#GET RID OF ENCODING ERRORS
# -*- coding: utf-8 -*-

"""
Translation is the shifting of object’s location.
If you know the shift in (x,y) direction, let it be (t_x,t_y), 
you can create the transformation matrix M as follows:

M = [[1,0,t_x],[0,1,t_y]]

You can take make it into a Numpy array of type np.float32 and pass it into cv2.warpAffine() function. 
See below example for a shift of (100,50):

IMPORTANT:
Third argument of the cv2.warpAffine() function is the size of the output image, 
which should be in the form of (width, height). 
Remember width = number of columns, and height = number of rows.
"""


import cv2
import numpy as np

img = cv2.imread('media/image.png',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols/2,rows/2))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
