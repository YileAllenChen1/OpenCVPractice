# reading, writing and showin images using cv2 imread, imwrite, imshow
import numpy as np
import cv2

img = cv2.imread('image.png',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('saved_image.png',img)
    cv2.destroyAllWindows() 

"""
#This method is deprecated

import cv2.cv as cv

# read image
image=cv.LoadImage('image.jpg', cv.CV_LOAD_IMAGE_COLOR)#Load the image
#Or just: image=cv.LoadImage('img/image.png')

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE) #Facultative
cv.ShowImage('a_window', image) #Show the image

# write image
cv.SaveImage("thumb.png", thumb)
cv.WaitKey(0) #Wait for user input and quit
"""