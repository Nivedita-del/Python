import cv2
import numpy as np
img = cv2.imread("1*mk1-6aYaf_Bes1E3Imhc0A.jpeg")
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
temp = cv2.imread("face.jpeg",0)

res = cv2.matchTemplate(grey_img,temp,cv2.TM_CCOEFF_NORMED)
print(res)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()