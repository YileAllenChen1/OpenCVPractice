import cv2
import numpy as np

cap =cv2.VideoCapture('media/test_video1.mov')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        print("No faces found")

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()




"""
hc = cv.Load("haarcascades/haarcascade_frontalface_alt.xml")

while True:
frame=cv.QueryFrame(capture)
faces = cv.HaarDetectObjects(frame, hc, cv.CreateMemStorage(), 1.2,2, cv.CV_HAAR_DO_CANNY_PRUNING, (0,0) )

for ((x,y,w,h),stub) in faces:
    cv.Rectangle(frame,(int(x),int(y)),(int(x)+w,int(y)+h),(0,255,0),2,0)

    cv.ShowImage("Window",frame)
    c=cv.WaitKey(1)
    if c==27 or c == 1048603: #If Esc entered
        break
"""