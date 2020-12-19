#!usr/bin/env python
#coding=utf-8

"""
use absdiff() on two frames to get a new image
apply grayscale and gaussian blue to new image
use goodFeaturesToTrack() to get strongest corners
calculate the average of the corners, through into queue
keep a queue with length 10, when the queue is full calculate the change of data to determine moving direction
"""

import cv2
import numpy as np
import Queue

camera = cv2.VideoCapture('media/movie1.mp4')
width = int(camera.get(3))
height = int(camera.get(4))

firstFrame = None
lastDec = None
firstThresh = None

feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

color = np.random.randint(0,255,(100,3))
num = 0

q_x = Queue.Queue(maxsize = 10)
q_y = Queue.Queue(maxsize = 10)

while True:
    (grabbed, frame) = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # Below is multiple ways to get binary threshold, effect are almost the same
    # thresh = cv2.adaptiveThreshold(frameDelta,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
              # cv2.THRESH_BINARY,11,2)
    # thresh = cv2.adaptiveThreshold(frameDelta,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    #           cv2.THRESH_BINARY,11,2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    p0 = cv2.goodFeaturesToTrack(thresh, mask = None, **feature_params)
    if p0 is not None:
        x_sum = 0
        y_sum = 0
        for i, old in enumerate(p0):
            x, y = old.ravel()
            x_sum += x
            y_sum += y
        x_avg = x_sum / len(p0)
        y_avg = y_sum / len(p0)

        if q_x.full():
            # print list(q_x.queue)
            qx_list = list(q_x.queue)
            key = 0
            diffx_sum = 0
            for item_x in qx_list:
                key +=1
                if key < 10:
                    diff_x = item_x - qx_list[key]
                    diffx_sum += diff_x
                    # print diff_x
            if diffx_sum < 0 and x_avg < 500:
                # print "some coming form left"
                cv2.putText(frame, "moving right", (100,100), 0, 0.5, (0,0,255),2)
            else:
                # print "right"
                cv2.putText(frame, "moving left", (100,100), 0, 0.5, (0,0,255),2)
            print x_avg
            q_x.get()
        q_x.put(x_avg)
        cv2.putText(frame, str(x_avg), (300,100), 0, 0.5, (0,0,255),2)
        frame = cv2.circle(frame,(int(x_avg),int(y_avg)),5,color[i].tolist(),-1)
  
    cv2.imshow("Video", frame)
    firstFrame = gray.copy()
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()
