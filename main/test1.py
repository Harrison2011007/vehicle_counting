import cv2
import numpy as np


# cap = cv2.VideoCapture("H:\\视频处理\\飞行记录文件\\2019-05-16宋楠楠-生态城\\100MEDIA\\DJI_0003.MOV")
# while True:
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1)&0xff == ord('q'):
# #         break
# img = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG',cv2.IMREAD_COLOR)

# cv2.line(img,(0,0),(150,150),(255,255,255),15)
# cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)
# cv2.circle(img,(100,63), 55, (0,255,0), -1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpencvCV tuts!',(0,130),font,1,(200,255,155),2,cv2.LINE_AA)
# px = img[55,55]
# img[55,55] = [255,255,255]
# px = img[55,55]
# print(px)
# px = img[100:150,100:150]
# print(px)
# print(img.shape)
# print(img.size)
# print(img.dtype)
# watch_face = img[37:111,107:194]
# img[0:74,0:87] = watch_face
#叠加图片
# cv2.imshow('image',img)
# img1 = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG')
# img2 = cv2.imread('E:\\work2019\\Mar\\images\\4.jpg')
# # weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols]
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# mask_inv = cv2.bitwise_not(mask)# Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)# Take only region of logo from logo
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows,0:cols] = dst
# cv2.imshow('res',img1)
# 阈值
# img = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG')
# retval,threshold = cv2.threshold(img,12,192,cv2.THRESH_BINARY)
# cv2.imshow('original',img)
# cv2.imshow('threshold',threshold)
# img = cv2.imread('E:\\work2019\\Mar\\images\\1.jpg')
# grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,threshold= cv2.threshold(grayscaled,10,155,cv2.THRESH_BINARY)
# cv2.imshow('Original',img)
# cv2.imshow('threshold',threshold)
# cap = cv2.VideoCapture("H:\\视频处理\\飞行记录文件\\2019-05-16宋楠楠-生态城\\100MEDIA\\DJI_0003.MOV")
img = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG')

# while(1):
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     dark_red = np.uint8([[[12, 22, 121]]])
#     dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)
#     lower_red = np.array([12,22,121])
#     upper_red = np.array([255,255,0])
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     res = cv2.bitwise_and(frame,frame, mask= mask)
#     cv2.imshow('frame', frame)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
# while(1):
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     low_red = np.array([30,150,50])
#     upper_red = np.array([255,255,180])
#     mask = cv2.inRange(hsv,low_red,upper_red)
#     res = cv2.bitwise_and(frame,frame,mask=mask)
#     kernel = np.ones((5,5),np.uint8)
#     opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
#     closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
#     cv2.imshow('Original', frame)
#     cv2.imshow('Mask', mask)
#     cv2.imshow('Opening', opening)
#     cv2.imshow('Closing', closing)
#     # cv2.imshow('Erosion', erosion)
#     # cv2.imshow('Dilation', dilation)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
# while(1):
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     lower_red = np.array([30,150,150])
#     upper_red = np.array([255,255,180])
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#     cv2.imshow('Original', frame)
#     edges = cv2.Canny(frame,240,1320)
#     cv2.imshow('Edges', edges)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27: break

# while(1):
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     template = cv2.imread('E:\\work2019\\Mar\\images\\car.jpg', 0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
#     threshold = 0.8
#     loc = np.where(res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img,pt,(pt[0] + w,pt[1] + h),(0,255,255),2)
#     cv2.imshow("Detected", img)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()
# # cap.release()

