import cv2
import mediapipe as mp
import os
import numpy 

capture=cv2.VideoCapture(1)

while True:
    success,img=capture.read()
    cv2.imshow('Counter',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()