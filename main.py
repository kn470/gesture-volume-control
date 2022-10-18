import cv2
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, COMError
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame, flipType=False)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        index_x, index_y = lmList[8][0:2]
        thumb_x, thumb_y = lmList[4][0:2]
        mid_x, mid_y = lmList[12][0:2]

        ind_dist = (abs(thumb_x - index_x)**2 + abs(thumb_y - index_y)**2)**0.5
        mid_dist = (abs(thumb_x - mid_x)**2 + abs(thumb_y - mid_y)**2)**0.5
        #print(dist)
        
        if ind_dist < 20:
            pyautogui.press("volumedown")
            cv2.circle(frame, (index_x,index_y), 3, (255,0,0))
        if mid_dist < 20:
            pyautogui.press("volumeup")
            cv2.circle(frame, (mid_x,mid_y), 3, (0,255,0))
    cv2.imshow("camera", frame)

    cv2.waitKey(1)

cv2.destroyAllWindows()