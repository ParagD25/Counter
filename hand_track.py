import cv2
import mediapipe as mp
import time

capture=cv2.VideoCapture(1)

while True:
    success,img=capture.read()