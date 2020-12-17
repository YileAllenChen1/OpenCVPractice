#GET RID OF ENCODING ERRORS
# -*- coding: utf-8 -*-

"""
Rotation of an image for an angle θ (theta) is achieved by the transformation matrix of the form

M = [[cosθ, -sinθ], [sinθ, cosθ]]

But OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer. 
Modified transformation matrix is given by

[[α β (1 - α)·center.x - β·center.y],[-β α β·center.x + (1-α)·center.y]]

where: α = scale·cosθ, β = scale·sinθ

To find this transformation matrix, OpenCV provides a function, cv2.getRotationMatrix2D.
Check below example which rotates the image by 90 degree with respect to center without any scaling.
"""
import cv2

img = cv2.imread('image.png',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
