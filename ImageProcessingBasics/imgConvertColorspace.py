import cv2

img=cv2.imread('media/image.png',cv2.IMREAD_COLOR)

result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # HLS, HSV, YCrCb, ....
cv2.imshow("CvtColor", result)
cv2.waitKey(0)


"""
To get other color flags, run:

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags
"""