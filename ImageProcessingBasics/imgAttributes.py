# getting image shape, size, dtype
import cv2

img = cv2.imread('media/image.png')

print img.shape
print img.size
print img.dtype
# uint8
# dtype is important for debugging