import cv2
import numpy as np

img = cv2.imread('Screenshot from 2020-04-26 12-36-29.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edge, 1, np.pi /180, threshold=255)

for line in lines:
    rho,theta = lines[1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    #x1 stores rounded off value of (r* cos(theta)-1000 * sin(theta))
    x1 = int(x0+100*(-b))
    #y1 stores the rounded off val of (r*sin(theta)+ 1000+cos(theta))
    y1 = int(y0 + 1000 * (a))
    #x2 stores the rounded off value of (r* cos(theta)+ 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off val of (r*sin(theta)+ 1000+cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img,(x1,y1),(x2,y2),(0.0,225),2)

cv2.imshow('img',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()