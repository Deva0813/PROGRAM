import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\devas\\Documents\\PROGRAM\\Python\\EX\\haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("output", img)
    print(img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
