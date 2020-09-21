import cv2
import numpy as np
img = cv2.imread("1*mk1-6aYaf_Bes1E3Imhc0A.jpeg")
lr = cv2.pyrDown(img)
lr_1 = cv2.pyrDown(lr)
hr = cv2.pyrUp(img)
cv2.imshow("Original Image",img)
cv2.imshow("pyr down Image",lr)
cv2.imshow("pyr down Image_1",lr_1)
cv2.imshow("pyr up",hr)
cv2.waitKey(0)
cv2.destroyAllWindows()
