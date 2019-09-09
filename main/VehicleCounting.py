import random
import cv2
import numpy as np


cap = cv2.VideoCapture("H:\\视频处理\\飞行记录文件\\2019-05-16宋楠楠-生态城\\100MEDIA\\DJI_0003.MOV")

#w = cap.get(3)#get width
#h = cap.get(4)#get height
#mx = int(w/2)
#my = int(h/2)

while cap.isOpened():
    ret,frame = cap.read()
    try:
        # cv2.imshow('Frame',frame)
        frame2 = frame
    except:
        print('EOF')
        break

    line1 = np.array([[100,100],[350,100],[350,200]],np.int32).reshape(-1,1,2)
    line2 = np.array([[400,50], [450, 300],], np.int32).reshape(-1, 1, 2)

    frame2 = cv2.polylines(frame2,[line1],False,(255,0,0),thickness=2)
    frame2 = cv2.polylines(frame2, [line2], False, (0, 255, 0), thickness=1)

    cv2.imshow('Frame 2',frame2)
    #abort and exit with "Q" or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release the window
cv2.destroyAllWindows() #close all openCV windows