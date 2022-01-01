import cv2
import mediapipe as mp
import os
import numpy 

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('Counter',frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()