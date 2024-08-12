
    
def Detect_Color_side(slfe,img):
    fgmask = fgbg.apply(img)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    (thresh, im_bw) = cv2.threshold(fgmask, 1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    mask_BG = cv2.bitwise_and(img,img,mask = im_bw)
    # cv2.imshow("dhjchj",cv2.resize(im_bw,(640,360)))
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # cv2.imshow("dhjchj",cv2.resize(hsv,(640,360)))

    #Green color
    # mahidol
    # lower_green = np.array([38,135,62])
    # upper_green = np.array([43,179,255])

    # large chessboard
    # lower_green = np.array([37,91,110])
    # upper_green = np.array([59,171,255])

    lower_green = np.array([53,92,34])
    upper_green = np.array([63,147,255])

    mask_color = cv2.inRange(hsv,lower_green,upper_green)
    cnts1,_ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            
    #Yellow color
    # mahidol
    # lower_yellow = np.array([24,130,148])
    # upper_yellow = np.array([29,193,255])

    # large chessboard
    # lower_yellow = np.array([30,90,181])
    # upper_yellow = np.array([41,107,255])
    lower_yellow = np.array([25,101,107])
    upper_yellow = np.array([35,123,255])

    mask_color2 = cv2.inRange(hsv,lower_yellow,upper_yellow)
    cnts2,_ = cv2.findContours(mask_color2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #Pink color
    # mahidol
    # lower_pink = np.array([165,152,84])
    # upper_pink = np.array([179,223,255])

    # large chessboard
    # lower_pink = np.array([123,88,81])
    # upper_pink = np.array([170,194,255])

    lower_pink = np.array([155,101,140])
    upper_pink = np.array([179,185,255])

    mask_color3 = cv2.inRange(hsv,lower_pink,upper_pink)
    cnts3,_ = cv2.findContours(mask_color3, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    return cnts1,cnts2,cnts3

def Detect_Color_top(img):
    fgmask = fgbg.apply(img)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    (thresh, im_bw) = cv2.threshold(fgmask, 1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    mask_BG = cv2.bitwise_and(img,img,mask = im_bw)
    # cv2.imshow("dhjchj",cv2.resize(im_bw,(640,360)))
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # cv2.imshow("dhjchj",cv2.resize(hsv,(640,360)))
    
    #Green color
    # mahidol
    # lower_green = np.array([46,55,42])
    # upper_green = np.array([59,129,255])
    
    # large chessboard
    # lower_green = np.array([22,105,34])
    # upper_green = np.array([33,174,255])
    
    lower_green = np.array([44,64,74])
    upper_green = np.array([65,160,255])
    
    mask_color = cv2.inRange(hsv,lower_green,upper_green)
    cnts1,_ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            
    #Yellow color
    # mahidol
    # lower_yellow = np.array([37,87,21])
    # upper_yellow = np.array([43,139,255])
    
    # large chessboard
    # lower_yellow = np.array([32,33,107])
    # upper_yellow = np.array([39,107,255])
    
    lower_yellow = np.array([32,33,107])
    upper_yellow = np.array([39,107,255])
    
    mask_color2 = cv2.inRange(hsv,lower_yellow,upper_yellow)
    cnts2,_ = cv2.findContours(mask_color2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #Pink color
    # mahidol
    # lower_pink = np.array([156,93,33])
    # upper_pink = np.array([169,193,255])
    
    # large chessboard
    # lower_pink = np.array([68,66,166])
    # upper_pink = np.array([179,161,255])
    
    lower_pink = np.array([163,60,61])
    upper_pink = np.array([179,154,255])
    
    mask_color3 = cv2.inRange(hsv,lower_pink,upper_pink)
    cnts3,_ = cv2.findContours(mask_color3, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    return cnts1,cnts2,cnts3

def Momets_contour(cnts,J,img):
    global color_circle,color_contours,color_plot, frame
    if len(cnts) > 0 :    
        c = max(cnts, key=cv2.contourArea)
        area = cv2.contourArea(c)
        if len(c) > 6 and area > 5:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"]) 
                cY = int(M["m01"] / M["m00"])
                if cX <= WIDTH and cX >= 0 and cY <= HEIGHT and cY >= 0 :
                    J.append([frame, (cX, cY)])
                    # print(J[-1],cv2.contourArea(c),len(c))
                    cv2.drawContours(img,[c],-1,color=color_contours,thickness=2)
                    cv2.circle(img,(cX,cY), radius=0, color=color_circle, thickness=5)  
    
    for idx, pos in J:
        cv2.circle(img, pos, radius=0, color=color_plot, thickness=4) 
        
    pts1 = np.array([pos for idx, pos in J], np.int32)
    pts1 = pts1.reshape((-1, 1, 2))   
    cv2.polylines(img,[pts1],isClosed = False,color=color_plot,thickness=2)
        
    return J,img


while True:
    succ_side,img_side = cap_side.read()
    succ_top,img_top = cap_top.read()
    
    if not succ_side or not succ_top :
        break
    
    img_side = cv2.resize(img_side,(WIDTH,HEIGHT))
    img_top = cv2.resize(img_top,(WIDTH,HEIGHT))
    cnts_t1,cnts_t2,cnts_t3 = Detect_Color_top(img_top)
    cnts_s1,cnts_s2,cnts_s3 = Detect_Color_side(img_side)
    
    
    #Green color
    color_circle = (255, 0, 0)
    color_contours = (0, 0, 255)
    color_plot = (0, 255, 0)
    J_s1,img_side = Momets_contour(cnts_s1,J_s1,img_side)
    J_t1,img_top = Momets_contour(cnts_t1,J_t1,img_top)
    
    
    #Yellow color
    color_circle = (255, 0, 0)
    color_contours = (0, 255, 0)
    color_plot = (255,0,0)
    J_s2,img_side = Momets_contour(cnts_s2,J_s2,img_side)
    J_t2,img_top = Momets_contour(cnts_t2,J_t2,img_top)
    
    
    #Pink color
    color_circle = (255, 0, 0)
    color_contours = (0, 255, 0)
    color_plot = (0,0,255)
    J_s3,img_side = Momets_contour(cnts_s3,J_s3,img_side)
    J_t3,img_top = Momets_contour(cnts_t3,J_t3,img_top)
    
    
    # cv2.putText(img_side,"FPS:{}".format(fps),(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
    # # write the flipped frame
    # out1.write(img_side)
    # out2.write(img_top)
                
    result = np.vstack([img_side,img_top])
    cv2.imshow('Frame',cv2.resize(result,(640,720)))
    
    count += 1
    if time.time() - timer >= 1 :
        fps = count
        count = 0
        timer = time.time()

    frame += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q') or frame > 5*60:
        break

G_real_idx, G_real_pos = get_real_pos(J_s1,J_t1)
Y_real_idx, Y_real_pos = get_real_pos(J_s2,J_t2)
P_real_idx, P_real_pos = get_real_pos(J_s3,J_t3)


# import pickle

# with open("GYP.coor", "wb") as file:
#     pickle.dump([(G_real_idx, G_real_pos), (Y_real_idx, Y_real_pos), (P_real_idx, P_real_pos)],file)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(Y_real_pos[:, 0], Y_real_pos[:, 1], Y_real_pos[:, 2])
ax.plot(G_real_pos[:, 0], G_real_pos[:, 1], G_real_pos[:, 2])
ax.plot(P_real_pos[:, 0], P_real_pos[:, 1], P_real_pos[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d( -400, 400)
ax.set_ylim3d(-400, 300)
ax.set_zlim3d( -100, 300)


fig0 = plt.figure()
x, y = th_in_dist(G_real_pos, G_real_idx, P_real_pos, P_real_idx)
ax1 = fig0.add_subplot(211)
ax1.plot(np.array(x)/60,np.array(y))
ax1.scatter(np.array(x)/60,np.array(y))
ax1.set_ylabel('Distance(mm)')
# ax1.set_ylim(0,160)

win, v = velocity(Y_real_idx, Y_real_pos)
ax2 = fig0.add_subplot(212)
ax2.plot(np.array(win)/60,np.array(v)*60)
ax2.scatter(np.array(win)/60,np.array(v)*60)
ax2.set_ylabel('Velocity(mm/sec)')
# ax2.set_ylim(0,20)

fig = plt.figure()
ax3 = fig.add_subplot(311)
ax3.plot(Y_real_idx/60, Y_real_pos[:, 0])
ax3.scatter(Y_real_idx/60, Y_real_pos[:, 0])
# ax3.set_ylim(0, 300)

ax4 = fig.add_subplot(312)
ax4.plot(Y_real_idx/60, Y_real_pos[:, 1])
ax4.scatter(Y_real_idx/60, Y_real_pos[:, 1])
# ax4.set_ylim(0, 300)

ax5 = fig.add_subplot(313)
ax5.plot(Y_real_idx/60, Y_real_pos[:, 2])
ax5.scatter(Y_real_idx/60, Y_real_pos[:, 2])
# ax5.set_ylim(0,250)
# ax5.set_xlabel('Frame')
# ax5.set_ylabel('Level(mm)')

plt.show()

cap_side.release()
cap_top.release()
# out.release()
cv2.destroyAllWindows()

