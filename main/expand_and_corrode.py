import cv2
import numpy as np

img = cv2.imread("E:\\work2019\\Mar\\images\\1.jpg")
ret,threshl = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1)

dilation = cv2.dilate(img,kernel,iterations=1)

cv2.imwrite("E:\\work2019\\Mar\\images\\erosion.jpg",erosion)
cv2.imwrite("E:\\work2019\\Mar\\images\\dilation.jpg",dilation)
