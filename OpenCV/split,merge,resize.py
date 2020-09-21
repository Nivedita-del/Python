import numpy as np
import cv2

img = cv2.imread('roi.jpg')

print(img.shape)# returns a tuple of number of rows,colums and channels
print(img.size)# total number of pixels
print(img.dtype)# returns image datatype is obtaines
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
