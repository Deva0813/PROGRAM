'''
import cv2
image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")

(h, w, d)= image.shape

print("width={},height={},depth={}".format(w,h,d))

cv2.imshow("image",image)
cv2.waitKey(0)

import cv2
image = cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")

(B,G,R) = image[100,50]

print("R={},G={},B={}".format(R,G,B)) 


import cv2
import os

image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")

roi= image[70:170,440:540]
cv2.imshow("Cropped",roi)
cv2.waitKey(0)

import cv2

image = cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
resize= cv2.resize(image,(10,10))
cv2.imshow("resized",resize)
cv2.waitKey(0)


import cv2

image = cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
(h,w,d) = image.shape

r=300.0 / w

dim = (300,int(h*r))
resized = cv2.resize(image, dim)
cv2.imshow("Resized",resized)
cv2.waitKey(0)

import cv2

image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
(h,w,d) = image.shape

center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center,-45,1.0)
rotated=cv2.warpAffine(image, M,(w,h))
cv2.imshow("Rotated",rotated)
cv2.waitKey(0)

import cv2
image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
blurred = cv2.GaussianBlur(image,(11,11),0)

cv2.imshow("Blurred",blurred)
cv2.waitKey(0)

import cv2
image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
output=image.copy()
cv2.rectangle(output,(450,80),(550,180),(255,255,255),2)
cv2.imshow("Rectangle",output)
cv2.waitKey(0)

import cv2
image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
output=image.copy()
cv2.circle(output,(300,150),100,(255,255,0),-1)
cv2.imshow("Circle",output)
cv2.waitKey(0)

import cv2
image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
output=image.copy()
cv2.line(output,(300,150),(100,600),(255,255,0),5)
cv2.imshow("Circle",output)
cv2.waitKey(0)

import cv2
image= cv2.imread("C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\12.jpg")
output=image.copy()
cv2.putText(output,"Hii....",(200,300),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,45),2)
cv2.imshow("Text",output)
cv2.waitKey(0)

import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="input image")
args= vars(ap.parse_args())

image =cv2.imread(args["image"])
cv2.imshow("image",image)
cv2.waitKey(0)

gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

edged= cv2.Canny(gray,30,150)
cv2.imshow("Edged",edged)
cv2.waitKey(0)

thresh= cv2.threshold(gray,255,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output=image.copy()

for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)
    cv2.imshow("Countours",output)
    cv2.waitKey(0)

text= "there are {} objects".format(len(cnts))
cv2.putText(output,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)
cv2.imshow("Contours",output)
cv2.waitKey(0)

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="input image")
ap.add_argument("-r","--radius",type=int,help="radius")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

orig=image.copy()
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

gray=cv2.GaussianBlur(gray,(args["radius"],args["radius"]),0)
(minVal,maxVal,minLoc,maxLoc)=cv2.minMaxLoc(gray)
image=orig.copy()

cv2.circle(image, maxLoc,args["radius"],(255,0,0),2)
cv2.imshow("output",image)
cv2.waitKey(0)

from cProfile import label
from imutils.video import VideoStream
from imutils.video import FPS
import time
import imutils
import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-p","--prototxt",required=True ,help="Prototext File")
ap.add_argument("-m","--model",required=True,help="model file")
ap.add_argument("-c","--confidence",type=float,default=0.2,help="ThresHold")
args= vars(ap.parse_args())

CLASSES = ["background","aeroplane","bicycle","bird","boat","bottle","bus","car","cat","chair","cow","diningtable","dog","horse","motorbike","preson", "pttrdplant","sheep","sofa","train","tvmonitor"]

COLORS=np.random.uniform(0,255,size=(len(CLASSES),3))

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototct"],args["model"])

print("[INFO] starting Video stream...")
vs= VideoStream(src=()).start()
time.sleep(2.0)
fps=FPS().start()

while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=400)
    (h,w)=frame.shape[:2]
    blob=cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)),0.007843,(300,300),1)
    net.setInput(blob)
    detections=net.forward()

    for i in np.arange(0,detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>args["confidence"]:
            idx = int(detections[0,0,i,1])
            box=detections[0,0,i,3:7]*np.array([w,h,w,h])
            (startX,startY,endX,endY)=box.astype("int")

            lable="{}:{:.2f}%".format(CLASSES[idx],confidence*100)
            print("[INFO] {}".format(lable))
            cv2.rectangle(frame,(startX,startY),(endX,endY),COLORS[idx],2)
            y=startY-15 if startY-15 else startY+15

            cv2.putText(frame,label,(startX,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)
            cv2.imshow("Frame",frame)
            key=cv2.waitKey(1) & 0xFF
            if key ==ord("q"):
                break
            fps.update()
            fps.stop()

            print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
            print("[INFO] approx. FPS{:.2f}".format(fps.fps()))

            cv2.destroyAllWindows
            vs.stop()
'''

















































































