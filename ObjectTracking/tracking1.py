import cv2
import numpy as np
import time

cap = cv2.VideoCapture('media/movie4.mp4')

#initialize the first frame to empty, help us obtain the fund
background = None

while 1:
    image, frame = cap.read()

    #if end of video, leave
    if not image:
        break
    
    #convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #smooth to remove noise
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    #if not yet obtain fund, continue, it will be first frame we get
    if background is None:
        background = gray
        continue
    
    #calculate differece between background and current frame
    subtraction = cv2.absdiff(background, gray)

    #apply threshold
    threshold = cv2.threshold(subtraction, 25, 255, cv2.THRESH_BINARY)[1]
    #print(threshold)
    #expand the threshold to cover holes
    threshold = cv2.dilate(threshold, None, iterations=2)

    #copy the threshild to detect contour
    contourImg = threshold.copy()

    #look for contour in image
    outlines, hierarchy = cv2.findContours(contourImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #go through all contours found
    for c in outlines:
        #remove smallest contour
        if cv2.contourArea(c) < 500:
            continue
    
        #obtain bounds of contour, the largest rectangle that encompasses the contour
        (x,y,w,h) = cv2.boundingRect(c)

        #draw the rectangle of the bounds
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)

    #show the images of video, threshold and subctraction
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Subtraction", subtraction)
    cv2.imshow("Contour", contourImg)
    cv2.imshow("Video", frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

