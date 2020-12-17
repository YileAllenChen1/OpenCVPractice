"""
Preferable interpolation methods are cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. 
By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes. 
"""

import cv2
import numpy as np

img = cv2.imread("image.png") #get the image

height, width = img.shape[:2]
resize = cv2.resize(img,(width/4, height/4), interpolation = cv2.INTER_CUBIC)

# Or:
#resize = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow('Hello World', resize) #Show the image

cv2.waitKey(0)

"""
import cv2.cv as cv

im = cv.LoadImage("img/alkaline.jpg") #get the image

thumb = cv.CreateImage((im.width / 2, im.height / 2), 8, 3) #Create an image that is twice smaller than the original

cv.Resize(im, thumb) #resize the original image into thumb
#cv.PyrDown(im, thumb)

cv.SaveImage("thumb.png", thumb) # save the thumb image
cv2:
import cv2
import numpy as np
img = cv2.imread('messi5.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
"""