import cv2

img = cv2.imread('image.png')
b,g,r = cv2.split(img)
merged = cv2.merge((b,g,r))

cv2.imshow("b", b) # remove blue
cv2.imshow("g", g) # remove green
cv2.imshow("r", r) # remove red
cv2.imshow("Merged", merged)
cv2.waitKey(0)