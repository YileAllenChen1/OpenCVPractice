# Detect blue color in a video

import cv2
import numpy as np

cap = cv2.VideoCapture('media/runeDemo.mp4')
#print(cap.isOpened()) # False
#print(cap.read()) # (False, None)
while(1):

    # read every frame
    _, frame = cap.read()

    # transfrom image from BGR to HSV colospace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define red region in HSV space
    lower_blue = np.array([110,50,50])       # red: 170
    upper_blue = np.array([130,255,255])     # red: 180

    # get blue portions based on defined threshold
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
