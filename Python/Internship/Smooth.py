import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="C:\\Users\\devas\\Documents\\PROGRAM\\Python\\Internship\\jeep.jpg",help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)