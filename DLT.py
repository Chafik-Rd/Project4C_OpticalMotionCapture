import pickle as pk
import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt


class DLT():
    def __init__(self,img1,img2,W_board,H_board,degree_XZ,size_sq,xyz_offset=(0,0,0),file_name=None) -> None:
        if file_name is not None:
            with open(file_name,"rb") as file:
                self.L,self.R = pk.load(file)
        else:   
            self.L = None
            self.R = None
        self.size_sq = size_sq  
        img_gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img_gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage1) = cv2.threshold(img_gray1, 127, 255, cv2.THRESH_BINARY)
        (thresh, blackAndWhiteImage2) = cv2.threshold(img_gray2, 127, 255, cv2.THRESH_BINARY)
        ret1, self.corners1original = cv2.findChessboardCorners(img_gray1,(W_board, H_board),None)
        ret2, self.corners2original = cv2.findChessboardCorners(img_gray2,(W_board, H_board),None)
        if not ret1 or not ret2:
            raise ValueError("Can't detect chessboard in img1:", ret1, " and img2:", ret2)
        self.corners1 = self.corners1original.reshape(H_board*W_board, 2)
        self.corners2 = self.corners2original.reshape(H_board*W_board, 2)
        # print(self.corners2.shape, self.corners2original.shape)
        
        x = []
        y = []
        z = []
        for r in range(H_board):
            for c in range(W_board):
                p_x = (-size_sq*r*math.cos(math.radians(degree_XZ))) + xyz_offset[0]
                p_y = (-size_sq*c) + xyz_offset[1]
                p_z = (-size_sq*r*math.sin(math.radians(degree_XZ))) + xyz_offset[2]
                
                p_x , p_y = self.rotate(p_x,p_y,30)
                p_z , p_y = self.rotate(p_z,p_y,60)
                
                x.append(p_x)
                y.append(p_y)
                z.append(p_z)
                
        self.x = np.array(x)
        self.y = np.array(y)
        self.z = np.array(z)
        self.all_idx = np.array(range(len(self.corners1)))
        self.origin = None
        
    def rotate(self,x,y,degree_XY):
        tx = x
        ty = y
        x = (tx * math.cos(math.radians(degree_XY))) - (ty*math.sin(math.radians(degree_XY)))
        y = (tx * math.sin(math.radians(degree_XY))) + (ty*math.cos(math.radians(degree_XY)))  
        
        return x , y
        
    def calibrate(self):
        uL = self.calibrate_uL
        vL = self.calibrate_vL
        uR = self.calibrate_uR
        vR = self.calibrate_vR
        x = self.calibrate_x
        y = self.calibrate_y
        z = self.calibrate_z
        if len(uL) ==  len(vL) and len(uL) == len(uR) and len(uL) == len(vR) and len(uL) == len(x) and len(uL) == len(y) and len(uL) == len(z):
            F_L = []
            F_R = []
            g_L = []
            g_R = []
            for i in range(len(uL)):
                F_L.append([x[i],y[i],z[i],1,0,0,0,0,-uL[i]*x[i],-uL[i]*y[i],-uL[i]*z[i]])
                F_L.append([0,0,0,0,x[i],y[i],z[i],1,-vL[i]*x[i],-vL[i]*y[i],-vL[i]*z[i]])
                
                F_R.append([x[i],y[i],z[i],1,0,0,0,0,-uR[i]*x[i],-uR[i]*y[i],-uR[i]*z[i]])
                F_R.append([0,0,0,0,x[i],y[i],z[i],1,-vR[i]*x[i],-vR[i]*y[i],-vR[i]*z[i]])

                g_L.extend([uL[i],vL[i]]) #หยิบที่ละตัว
                g_R.extend([uR[i],vR[i]])

            F_L = np.array(F_L)
            F_R = np.array(F_R)
            g_L = np.array([g_L]).T
            g_R = np.array([g_R]).T
            
            self.L = np.dot(np.dot(np.linalg.pinv(np.dot(F_L.T,F_L)),F_L.T),g_L).T[0]
            self.R = np.dot(np.dot(np.linalg.pinv(np.dot(F_R.T,F_R)),F_R.T),g_R).T[0]
            
    def get_XYZ(self,uL,vL,uR,vR, useOrigin  = False):
        L = self.L
        R = self.R
        Q = np.array([[L[0]-(L[8]*uL),L[1]-(L[9]*uL),L[2]-(L[10]*uL)],
             [L[4]-(L[8]*vL),L[5]-(L[9]*vL),L[6]-(L[10]*vL)],
             [R[0]-(R[8]*uR),R[1]-(R[9]*uR),R[2]-(R[10]*uR)],
             [R[4]-(R[8]*vR),R[5]-(R[9]*vR),R[6]-(R[10]*vR)]])
        q = np.array([[uL-L[3]],
             [vL-L[7]],
             [uR-R[3]],
             [vR-R[7]]])
        
        xyz = np.dot(np.dot(np.linalg.pinv(np.dot(Q.T,Q)),Q.T),q).T[0]
        
        if useOrigin:
            if self.origin is None:
                raise ValueError("You must specified the uvL uvR of the origin")
            return xyz[0]-self.origin[0], xyz[1]-self.origin[1], xyz[2]-self.origin[2]
        return xyz
        
    def set_origin(self, uL,vL,uR,vR):
        self.origin = self.get_XYZ(uL,vL,uR,vR)
    
    def euclidean_dist(self, xyz, uvw):
        return  math.sqrt(pow(xyz[0]-uvw[0],2) + pow(xyz[1]-uvw[1],2) + pow(xyz[2]-uvw[2],2))
    
    def random_point(self,num_calib_point):
        # self.rand_idx = [30,  89,  35,  54,  68,  34,  37, 112, 113, 105,  93,  56,  18,47,  31,  78,  59,  81,  25,  42]
        # self.remain_idx = np.delete(self.all_idx, self.rand_idx)
        self.rand_idx = np.random.choice(self.all_idx, size=num_calib_point, replace=False)
        self.remain_idx = np.delete(self.all_idx, self.rand_idx)
        self.calibrate_x = self.x[self.rand_idx]
        self.calibrate_y = self.y[self.rand_idx]
        self.calibrate_z = self.z[self.rand_idx]
        rand_uvL = self.corners1[self.rand_idx]
        rand_uvR = self.corners2[self.rand_idx]
        self.calibrate_uL,self.calibrate_vL= zip(*rand_uvL.tolist())
        self.calibrate_uR,self.calibrate_vR= zip(*rand_uvR.tolist())
        
        self.test_x = self.x[self.remain_idx]
        self.test_y = self.y[self.remain_idx]
        self.test_z = self.z[self.remain_idx]
        remain_uvL = self.corners1[self.remain_idx]
        remain_uvR = self.corners2[self.remain_idx]
        self.test_uL,self.test_vL= zip(*remain_uvL.tolist())
        self.test_uR,self.test_vR= zip(*remain_uvR.tolist())
      
    def LR_minimum_err(self,start,stop,n):
        p_mean = np.Inf
        p_std = np.Inf
        tStart = time.time()
        run_times = (stop-start+1)*n
        c = 0
        for i in range(start,stop+1):
            d_n = np.arange(n,dtype=np.float64)
            for j in range(n):
                self.random_point(i)
                self.calibrate()
                d = np.arange(len(self.test_uL),dtype=np.float64)
                for k in range(len(self.test_uL)):
                    q = self.get_XYZ(self.test_uL[k],self.test_vL[k],self.test_uR[k],self.test_vR[k])
                    d[k] = self.euclidean_dist(q, [self.test_x[k], self.test_y[k], self.test_z[k]])
                
                if np.mean(d) < p_mean and np.std(d) < p_std and np.mean(d<0.04*self.size_sq) > 0.6:
                    self.best_index = self.rand_idx
                    self.best_LR = (self.L,self.R)
                    p_mean = np.mean(d)
                    p_std = np.std(d)
                    self.best = {"best_index":self.rand_idx,"best_LR":(self.L,self.R),"mean":p_mean,"p_std":p_std,"d":d}
                    
                d_n[j] = np.mean(d)
                c += 1
                percentComplete = (c/run_times) * 100
                percentRemaining = 100 - percentComplete
                
                elapseTime = time.time() - tStart
                remainningTime = (elapseTime / percentComplete) * percentRemaining
                
                remain_minute = remainningTime // 60
                remain_sec = remainningTime % 60
                
                form = (percentComplete, remain_minute, remain_sec)
                print("%9.5f%% complete, remainning time: %2.0dm %2.0ds"%form, end="\r")
            print(" "*100, end="\r")
            print(i,np.mean(d_n),np.std(d_n),min(d_n),max(d_n))
            
        self.L, self.R = self.best["best_LR"]
        
        with open("list_LR.param","wb") as file:
            pk.dump((self.L,self.R),file)
        
        return (self.L,self.R)
    
    def get_uv(self):
        uL = []
        vL = []
        uR = []
        vR = []
        x = self.x
        y = self.y
        z = self.z
        L = self.L
        R = self.R
        for i in range(len(x)):
            uL.append(int((L[0]*x[i] + L[1]*y[i] + L[2]*z[i] + L[3]) / (L[8]*x[i] + L[9]*y[i] + L[10]*z[i] + 1)))
            vL.append(int((L[4]*x[i] + L[5]*y[i] + L[6]*z[i] + L[7]) / (L[8]*x[i] + L[9]*y[i] + L[10]*z[i] + 1)))
            uR.append(int((R[0]*x[i] + R[1]*y[i] + R[2]*z[i] + R[3]) / (R[8]*x[i] + R[9]*y[i] + R[10]*z[i] + 1)))
            vR.append(int((R[4]*x[i] + R[5]*y[i] + R[6]*z[i] + R[7]) / (R[8]*x[i] + R[9]*y[i] + R[10]*z[i] + 1)))
        
        return uL,vL,uR,vR
if __name__ == "__main__":
    cap_top = cv2.VideoCapture("D:/Project4C/coding/Video_Test/64-10-18/top_60.MOV")
    cap_side = cv2.VideoCapture("D:/Project4C/coding/Video_Test/64-10-18/side.MOV")
    WIDTH  = 1920
    HEIGHT = 1080    
    # cap_top = cv2.VideoCapture("Video_Test/top_1.MOV")
    # cap_side = cv2.VideoCapture("Video_Test/side_1.MOV")    
    ret1,img1 = cap_side.read()
    ret2,img2 = cap_top.read()
    # img1 = cv2.resize(img1,(WIDTH,HEIGHT))
    # img2 = cv2.resize(img2,(WIDTH,HEIGHT))
    # img1 = cv2.imread('side.jpg')
    # img2 = cv2.imread('top.jpg')
    # x = []
    # y = []
    # z = []
    # for r in range(6):
    #     for c in range(9):
    #         z.append((-19.2857143*r)*math.sin(math.radians(80)))
    #         x.append((-19.2857143*r)*math.cos(math.radians(80)))
    #         y.append(-19.2857143*c)
    # x = np.array(x)
    # y = np.array(y)
    # z = np.array(z) 
    
    # fig = plt.figure()
    # ax = fig.add_subplot(projection="3d")
    # ax.scatter(x, y, z)
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')
    
    # ax.set_xlim3d(-100, 0)
    # ax.set_ylim3d(-100, 0)
    # ax.set_zlim3d(-100, 0)

    # plt.show()
    
    chess_dim = (9, 6)
    img_gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img_gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage1) = cv2.threshold(img_gray1, 127, 255, cv2.THRESH_BINARY)
    (thresh, blackAndWhiteImage2) = cv2.threshold(img_gray2, 127, 255, cv2.THRESH_BINARY)
    ret1, corners1 = cv2.findChessboardCorners( img_gray1,chess_dim,None)
    ret2, corners2 = cv2.findChessboardCorners( img_gray2,chess_dim,None)
    img_D1 = cv2.drawChessboardCorners(img1, chess_dim, corners1, ret1)
    img_D2 = cv2.drawChessboardCorners(img2, chess_dim, corners2, ret2)
    
    # dlt = DLT(img1,img2,15, 10, 50, 25) #mm
    # dlt.LR_minimum_err(20,20,2000)
    # print(dlt.best)
    
    # dlt.random_point(10)
    # dlt.calibrate()
    # print(dlt.get_XYZ(834.5,678,934.59125,745.49164))
    hStack = np.vstack([img_D1, img_D2]) 
    
    cv2.imshow("bnkjnjk",cv2.resize(hStack,(640,720)))
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()