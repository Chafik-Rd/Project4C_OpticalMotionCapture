
import cv2
import numpy as np

cap = cv2.VideoCapture("Video_Test/65-02-24/ชุด1/side.MOV")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
ret  = False

def setFrame(frame_nr):
    global cap, img, imgHSV, ret
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nr)
    ret, img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
def empty(a):
    pass

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',640,360)
cv2.createTrackbar('Frame','HSV',0,frame_count,setFrame)
cv2.createTrackbar('HUE Min','HSV',0,179,empty)
cv2.createTrackbar('HUE Max','HSV',179,179,empty)
cv2.createTrackbar('SAT Min','HSV',0,255,empty)
cv2.createTrackbar('SAT Max','HSV',255,255,empty)
cv2.createTrackbar('VALUE Min','HSV',0,255,empty)
cv2.createTrackbar('VALUE Max','HSV',255,255,empty)

while(True):
    h_min = cv2.getTrackbarPos('HUE Min','HSV')
    h_max = cv2.getTrackbarPos('HUE Max','HSV')
    s_min = cv2.getTrackbarPos('SAT Min','HSV')
    s_max = cv2.getTrackbarPos('SAT Max','HSV')
    v_min = cv2.getTrackbarPos('VALUE Min','HSV')
    v_max = cv2.getTrackbarPos('VALUE Max','HSV')
    print(h_min)
    if ret:
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        mask = cv2.inRange(imgHSV,lower,upper)
        result = cv2.bitwise_and(img,img,mask = mask)

        mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        hStack = np.hstack([mask,result])    

        cv2.imshow('Horizontal Stacking',cv2.resize(hStack,(1280,360)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
