import cv2
from matplotlib import pyplot as pt

img = cv2.imread('messi5.jpg')
higher_reso = cv2.pyrUp(img)


lower_reso = cv2.pyrDown(higher_reso)

pt.imshow(lower_reso)

