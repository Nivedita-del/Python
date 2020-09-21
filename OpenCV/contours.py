import numpy as np
import cv2

img = cv2.imread('opencv-logo-white.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hieratchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# contours is a python list of all contours in image. Each individual contour is a numpy(x,y) coordinates of boundary points of the object
#hierarchy is the optional output vector which is containing the information about the image topology
print("Number of contours = " + str(len(contours)))

#Print out the value of the individual contour
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Image',img)
cv2.imshow('Image Gray', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()