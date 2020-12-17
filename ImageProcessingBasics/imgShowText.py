# Output text info on image
import cv2
import numpy as np

image=cv2.imread('media/image.png', cv2.IMREAD_COLOR) #Load the image

# define text properties
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0, 0, 0)
fontCaption = "Display text"

height, width, channel = image.shape

y = height / 2 # y position of the text
x = width / 4 # x position of the text

cv2.putText(image, fontCaption, (x,y), fontface, fontscale, fontcolor) # add text to image
#cv2.putText(image, 'Hello World', (300,100), 0, 0.5, (0,0,255),2)

cv2.imshow('Hello World', image) #Show the image

cv2.waitKey(0)


"""
# depricated method
import cv2.cv as cv

image=cv.LoadImage('img/lena.jpg', cv.CV_LOAD_IMAGE_COLOR) #Load the image

font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font

y = image.height / 2 # y position of the text
x = image.width / 4 # x position of the text

cv.PutText(image,"Hello World !", (x,y),font, cv.RGB(255, 255, 255)) #Draw the text

cv.ShowImage('Hello World', image) #Show the image

cv.WaitKey(0)
cv2:
cv2.putText(frame, 'Hello World', (300,100), 0, 0.5, (0,0,255),2)
"""