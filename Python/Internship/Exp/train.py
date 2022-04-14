from dis import show_code
from functools import total_ordering
from multiprocessing.sharedctypes import copy
from turtle import Turtle
from charset_normalizer import detect
from cv2 import rectangle
from imutils.video import VideoStream
import argparse
import cv2
import time
import os
import imutils

ap=argparse.ArgumentParser()

ap.add_argument("-c","--cascade",required=True,help= "path to where the face cascade located")
ap.add_argument("-o","--output",required=True,help="path where the output to be stored")

args=vars(ap.parse_args())

detector= cv2.CascadeClassifier(args["cascade"])
print("[INFO] starting voideo stream...")
vs= VideoStream(src=0).start()
time.sleep(2.0)
total=0

while True:
    frame = vs.read()
    orig = frame.copy()
    frame=imutils.resize(frame,width=400)
    rects=detector.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),scaleFactor=1.1,minNeibhours=5,minSize=(30,30))

    for(x,y,w,h) in rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Frame",frame)
        key=cv2.waitKey(1) & 0xFF
        if key==ord("k"):
            p=os.path.sep.join([args["output"],"{}.png".format(str(total).zfill(5))])
            cv2.imwrite(p,orig)
            total+=1

        elif key==ord("q"):
            break

        print("[INFO] {} face image stored".format(total))
        print("[INFO] cleaning up..")
        cv2.destroyAllWindows()
        vs.stop()