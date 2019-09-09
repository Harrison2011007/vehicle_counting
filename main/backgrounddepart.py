import numpy as np
import  cv2

cap = cv2.VideoCapture("H:\\视频处理\\飞行记录文件\\2019-05-16宋楠楠-生态城\\100MEDIA\\DJI_0003.MOV")#openVideo file
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows= True) #Create the backGround substractor

while(cap.isOpened()):
    ret,frame = cap.read()#read a frame

    fgmask = fgbg.apply(frame)# use the substractor

    try:
        cv2.imshow('Frame',frame)
        cv2.imshow('Background Substraction',fgmask)
    except:
        #if there are no more frames to show
        print('EoF')
        break


    k = cv2.waitKey(30) & 0xff
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()
