import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import DLT
import math
import json
# from kalman import KalmanFilter

def COLOR(name, side_lower, side_upper, top_lower, top_upper, draw_color):
    color = {
        "name":name,
        "side":{
            "range":{
                "lower":np.array(side_lower),
                "upper":np.array(side_upper)
            },
            "marker_pos":[]
        },
        "top":{
            "range":{
                "lower":np.array(top_lower),
                "upper":np.array(top_upper)
            },
            "marker_pos":[]
        },
        "draw":draw_color
    }
    return color
        
def get_real_pos(J_s,J_t):
    frame_idxL, uvL = zip(*J_s)
    frame_idxR, uvR = zip(*J_t)
    # print(uvL)
    uvL = np.asarray(uvL)*scale_side
    uvR = np.asarray(uvR)*scale_top
    
    real_pos = []
    real_idx = []
    
    for idx in frame_idxL:
        if idx in frame_idxR:
            xyz = dlt.get_XYZ(uvL[frame_idxL.index(idx)][0], uvL[frame_idxL.index(idx)][1], uvR[frame_idxR.index(idx)][0], uvR[frame_idxR.index(idx)][1], useOrigin=False)
            xyz[2] , xyz[1] = dlt.rotate(xyz[2],xyz[1],-60)
            xyz[0] , xyz[1] = dlt.rotate(xyz[0],xyz[1],-30)
            real_idx.append([idx])
            real_pos.append(xyz)
    return np.array(real_idx), np.array(real_pos)

def euclidean_dist(xyz, uvw):
    return  math.sqrt(pow(xyz[0]-uvw[0],2) + pow(xyz[1]-uvw[1],2) + pow(xyz[2]-uvw[2],2))

def th_in_dist(thumb_pos, thumb_index, index_pos, index_index):
    thumb_index = thumb_index.tolist()
    thumb_pos = thumb_pos.tolist()
    index_index = index_index.tolist()
    index_pos = index_pos.tolist()
    dists = []
    index = []
    for idx in thumb_index:
        if idx in index_index:
            index.append(idx)
            dists.append(euclidean_dist(thumb_pos[thumb_index.index(idx)], index_pos[index_index.index(idx)]))
    return index, dists

def velocity(wrist_in, wrist_pos):
    v = [0]
    for idx in range(len(wrist_pos)-1):
        d = euclidean_dist(wrist_pos[idx+1], wrist_pos[idx])
        t = (wrist_in[idx+1] -  wrist_in[idx])
        v.append(d/t)
    return wrist_in, v

class Detect():
    def __init__(self, side_path, top_path, all_color, fps = None):
        self.cap_side = cv2.VideoCapture(side_path)
        self.cap_top = cv2.VideoCapture(top_path)
        
        self.video_framerate = fps
        
        self.scale_side = self.cap_side.get(cv2.CAP_PROP_FRAME_WIDTH)/WIDTH
        self.scale_top = self.cap_top.get(cv2.CAP_PROP_FRAME_WIDTH)/WIDTH 
        
        
        self.all_color = all_color

        # self.kalman_markers = [KalmanFilter(0.1, 1, 1, 1, 0.1, 0.1) for _ in self.all_color]
        
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)) 
        self.fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)
        
        self.frame = 0
        self.cam = None
        
    def get_img_for_calib(self):
        succ_side,img_side_cali = self.cap_side.read()
        succ_top,img_top_cali = self.cap_top.read()
        
        if succ_side and succ_top:
            return img_side_cali, img_top_cali
        raise ValueError("Can't load video")
    
    def set_frame(self, second):
        self.cap_side.set(cv2.CAP_PROP_POS_FRAMES, (second*self.video_framerate))
        self.cap_top.set(cv2.CAP_PROP_POS_FRAMES, (second*self.video_framerate))
        
    def detect_next_frame(self):
        succ_side,img_side = self.cap_side.read()
        succ_top,img_top = self.cap_top.read()
    
        if not succ_side or not succ_top :
            return False, None
        img_side = cv2.resize(img_side,(WIDTH,HEIGHT))
        img_top = cv2.resize(img_top,(WIDTH,HEIGHT))
        
        self.cam = {
            "side":img_side,
            "top":img_top
        }
        
        cnts_s = self.detect_color("side", self.all_color)
        cnts_t = self.detect_color("top", self.all_color)
        
        for idx, c in enumerate(self.all_color):
            self.momets_contour("side", cnts_s[idx], idx, 5, trail = "dot")
            self.momets_contour("top", cnts_t[idx], idx, 4, trail = "dot")
            
        self.frame += 1
        
        return True, list(self.cam.values())
        
    def detect_color(self,cam_name,color):
        fgmask = self.fgbg.apply(self.cam[cam_name])
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, self.kernel)
        (thresh, im_bw) = cv2.threshold(fgmask, 1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        mask_BG = cv2.bitwise_and(self.cam[cam_name],self.cam[cam_name],mask = im_bw)
        hsv = cv2.cvtColor(self.cam[cam_name],cv2.COLOR_BGR2HSV)
        cnts = []
        for c in color:
            mask_color = cv2.inRange(hsv,c[cam_name]["range"]["lower"],c[cam_name]["range"]["upper"])
            cnt,_ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            cnts.append(cnt)
        return cnts
    
    def momets_contour(self,cam_name,cnt,idx,c_area, trail = "line"):
        # x_k, y_k = self.kalman_markers[idx].predict()
        # x_k, y_k = int(x_k), int(y_k)
        if len(cnt) > 0 :    
            c = max(cnt, key=cv2.contourArea)
            area = cv2.contourArea(c)
            if len(c) > 6 and area > c_area:
                M = cv2.moments(c)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"]) 
                    cY = int(M["m01"] / M["m00"])
                    if cX <= WIDTH and cX >= 0 and cY <= HEIGHT and cY >= 0 :
                        x_k, y_k = cX, cY
        
                        # self.kalman_markers[idx].update(np.array([[x_k], [y_k]]))
                        self.all_color[idx][cam_name]["marker_pos"].append([self.frame, (x_k, y_k)])
                        # cv2.drawContours(self.cam[cam_name],[c],-1,color=self.all_color[idx]["draw"],thickness=4)
                        cv2.circle(self.cam[cam_name], (x_k, y_k), radius=0, color=self.all_color[idx]["draw"], thickness=7)  
                        
                        if trail is not None:
                            if trail is "dot":
                                for idex, pos in self.all_color[idx][cam_name]["marker_pos"]:
                                    cv2.circle(self.cam[cam_name], pos, radius=0, color=self.all_color[idx]["draw"], thickness=6) 
                            else:
                                pts1 = np.array([pos for idx, pos in self.all_color[idx][cam_name]["marker_pos"]], np.int32)
                                pts1 = pts1.reshape((-1, 1, 2))   
                                cv2.polylines(self.cam[cam_name],[pts1],isClosed = False,color=self.all_color[idx]["draw"],thickness=4)
 
    def export_marker_pos(self):
        all_marker = {}
        for c in self.all_color:
            all_marker[c["name"]] = {
                "side":c["side"]["marker_pos"],
                "top":c["top"]["marker_pos"]
            }
        
        # with open(folder + 'data7.json', 'w') as fp:
        #     json.dump(all_marker, fp)
            
        return all_marker

    def release(self):
        self.cap_side.release()
        self.cap_top.release()


if __name__ == '__main__':
    green = COLOR("green",side_lower=[36,79,65], 
                side_upper=[59,135,255], 
                top_lower=[39,65,126], 
                top_upper=[62,116,255], 
                draw_color=[255,0,0])
    # mahidol              
                #   side_lower=[38,135,62],
                #   side_upper=[43,179,255], 
                #   top_lower=[46,55,42], 
                #   top_upper=[59,129,255], 
                #   draw_color=[255,0,0])
    
    pink = COLOR("pink",side_lower=[162,107,112], 
                side_upper=[168,196,255], 
                top_lower=[145,25,112], 
                top_upper=[170,141,255], 
                draw_color=[0,255,0])
    # mahidol
                #  side_lower=[165,152,84],
                #  side_upper=[179,223,255], 
                #  top_lower=[156,93,33], 
                #  top_upper=[169,193,255], 
                #  draw_color=[0,255,0])
    
    yellow = COLOR("yellow",side_lower=[30,84,136], 
                side_upper=[37,150,255], 
                top_lower=[26,58,92], 
                top_upper=[36,123,255], 
                draw_color=[0,0,255])
    # mahidol
                #   side_lower=[24,130,148],   
                #   side_upper=[29,193,255], 
                #   top_lower=[37,87,21], 
                #   top_upper=[43,139,255], 
                #   draw_color=[0,0,255])

    all_color = [green,pink,yellow]

    WIDTH = 1280
    HEIGHT = 720
    # WIDTH = 1920
    # HEIGHT = 1080


    folder = "Video_Test/65-02-04/ชุด2/"
    side_path = folder + "side_60.MOV"
    top_path = folder + "top.MOV"

    dt = Detect(side_path, top_path, all_color, 60)
    scale_side, scale_top = dt.scale_side, dt.scale_top
    img_side_cali, img_top_cali = dt.get_img_for_calib()
    dt.set_frame(47)

    dlt = DLT.DLT(img_side_cali, img_top_cali, 15, 10, 50, 25,file_name="mean_LR")
    # mahidol
    # dlt = DLT.DLT(img_side_cali, img_top_cali, 9, 6, 45, 16.5555556)

    dlt.LR_minimum_err(20,20,2000)
    # print(dlt.best)
    # dlt.set_origin(1413, 946, 1440, 674)

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc('M','P','4','2')
    # out1 = cv2.VideoWriter('Video_Test/18-10-64/combined_P_9.mp4',fourcc, 60.0, (3840,1080))
    # out2 = cv2.VideoWriter('Video_Test/18-10-64/topP_7.mp4',fourcc, 60.0, (1280,720))
                    
    while True:
        succes, imgs = dt.detect_next_frame()

        if succes:
            img_side, img_top = imgs
        else:
            break
        
        # out1.write(img_side)
        # out2.write(img_top)
                    
        result = np.hstack([img_side,img_top])
        cv2.imshow('Frame',cv2.resize(result,(1280,360)))
            
        # out1.write(cv2.resize(result, (3840,1080)))
        
        
        if cv2.waitKey(1) & 0xFF == ord('q') or dt.frame > 5*60:
            break

    marker = dt.export_marker_pos()

    G_real_idx, G_real_pos = get_real_pos(marker["green"]["side"], marker["green"]["top"])
    Y_real_idx, Y_real_pos = get_real_pos(marker["yellow"]["side"], marker["yellow"]["top"])
    P_real_idx, P_real_pos = get_real_pos(marker["pink"]["side"], marker["pink"]["top"])

    import pickle

    with open("GYP.coor", "wb") as file:
        pickle.dump([(G_real_idx, G_real_pos), (Y_real_idx, Y_real_pos), (P_real_idx, P_real_pos)],file)


    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(Y_real_pos[:, 0], Y_real_pos[:, 1], Y_real_pos[:, 2])
    ax.plot(G_real_pos[:, 0], G_real_pos[:, 1], G_real_pos[:, 2])
    ax.plot(P_real_pos[:, 0], P_real_pos[:, 1], P_real_pos[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax.set_xlim3d( -400, 400)
    # ax.set_ylim3d(-400, 300)
    # ax.set_zlim3d( -100, 300)


    fig0 = plt.figure()
    x, y = th_in_dist(G_real_pos, G_real_idx, P_real_pos, P_real_idx)
    ax1 = fig0.add_subplot(311)
    ax1.plot(np.array(x)/60,np.array(y))
    ax1.scatter(np.array(x)/60,np.array(y))
    ax1.set_ylabel('Distance(mm)')
    # 
    # 

    win, v = velocity(Y_real_idx, Y_real_pos)
    ax2 = fig0.add_subplot(312)
    ax2.plot(np.array(win)/60,np.array(v)*60)
    ax2.scatter(np.array(win)/60,np.array(v)*60)
    ax2.set_ylabel('Velocity(mm/sec)')
    # ax2.set_ylim(0,20)


    ax3 = fig0.add_subplot(313)
    ax3.plot(G_real_idx/60, G_real_pos[:, 2])
    ax3.scatter(G_real_idx/60, G_real_pos[:, 2])
    # ax3.set_ylim(0,250)
    ax3.set_xlabel('Time(Sec)')
    ax3.set_ylabel('Level(mm)')

    plt.show()
    dt.release()
    # out1.release()
    # out2.release()
    cv2.destroyAllWindows()

