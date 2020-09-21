import cv2
import numpy as np

img = cv2.imread('roi.jpg')

print (img)

pix = img [100, 100]

print (pix)

ball = img[280:340, 330:390]
img[293:363,120:180] = ball
