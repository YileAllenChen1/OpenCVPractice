import cv2

cap = cv2.VideoCapture('ImageProcessingBasics/windmill.mp4')

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 10, 70)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow('Video feed', mask)
    
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()

"""
#cv version
import cv2.cv as cv

capture = cv.CaptureFromFile('img/myvideo.avi')

nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))
fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)
wait = int(1/fps * 1000/1)

dst = cv.CreateImage((int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH)),
                        int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))), 8, 1)

for f in xrange( nbFrames ):

    frame = cv.QueryFrame(capture)

    cv.CvtColor(frame, dst, cv.CV_BGR2GRAY)
    cv.Canny(dst, dst, 125, 350)
    cv.Threshold(dst, dst, 128, 255, cv.CV_THRESH_BINARY_INV)

    cv.ShowImage("The Video", frame)
    cv.ShowImage("The Dst", dst)
    cv.WaitKey(wait)
"""