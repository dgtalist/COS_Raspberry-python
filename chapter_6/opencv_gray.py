import cv2
import numpy as np

img = cv2.imread("파일명.확장자")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("파일명", img)
cv2.imshow("파일명 – gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
