import cv2
import numpy as np
from sklearn.metrics import pairwise

cap = cv2.VideoCapture(0)

kernelOpen= np.ones((5,5))

kernelClose= np.ones((20,20))

lb= np.array([20,100,100])

ub=np.array([120,255,255])

while True:
    ret,frame=cap.read()
    flip=cv2.flip(frame,1)
    flip=cv2.resize(flip,(500,400))

    imgSeg=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    imgSegflip=cv2.flip(imgSeg,1)
    imgSegflip=cv2.resize(imgSegflip,(500,400))

    mask=cv2.inRange(imgSegflip,lb,ub)
    mask=cv2.resize(mask,(500,400))

    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernelOpen)
    maskOpen=cv2.resize(mask,(500,400))
    maskClose=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernelClose)
    maskClose=cv2.resize(mask,(500,400))

    final=maskClose
    conts,h=cv2.findContours(maskClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    if(len(conts)!=0):
        b=max(conts,key=cv2.contourArea)
        west=tuple(b[b[:,:,0].argmin()][0])
        east=tuple(b[b[:,:,0].argmax()][0])
        north=tuple(b[b[:,:,1].argmin()][0])
        south=tuple(b[b[:,:,1].argmax()][0])
        centerx=(west[0]+east[0])/2
        centery=(north[0]+south[0])/2

        cv2.drawContours(flip,b,-1,(0,255,0),3)
        cv2.circle(flip,west,6,(0,0,255),-1)
        cv2.circle(flip,east,6,(0,0,255),-1)
        cv2.circle(flip,north,6,(0,0,255),-1)
        cv2.circle(flip,south,6,(0,0,255),-1)
        cv2.circle(flip,(int(centerx),int(centery)),6,(255,0,0),-1)
        
        cv2.imshow('video',flip)

        if cv2.waitKey(1) & 0xFF==ord(' '):
            break

cap.release()
cv2.destroyAllWindows()