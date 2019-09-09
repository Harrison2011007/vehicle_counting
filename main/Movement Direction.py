import numpy as np
import cv2
import car_package
import time

cap = cv2.VideoCapture("H:\\视频处理\\飞行记录文件\\2019-05-16宋楠楠-生态城\\100MEDIA\\DJI_0003.MOV")#open video file
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows= True) #create background substractor
kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)
#Variables
font = cv2.FONT_HERSHEY_SIMPLEX
cars = []
max_p_age = 5
pid = 1
areaTH = 500
while cap.isOpened():
    ret,frame = cap.read() # read a frame
    fgmask = fgbg.apply(frame)
    try:
        ret,imBin = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        #opening (erode->dilate)
        mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN,kernelOp)
        #closing(dilate -> erode)
        mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernelCl)
    except:
        #if there is no more frames to show
        print('EOF')
        break

    [_, contours0, hierarchy] = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours0:
        cv2.drawContours(frame,cnt,-1,(0,255,0),3,8)
        area = cv2.contourArea(cnt)
        if area > areaTH:
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m10'] / M['m00'])
            x, y, w, h = cv2.boundingRect(cnt)

            new = True
            for i in cars:
                if abs(x-i.getX()) <= w and abs(y-i,getY()) <= h:
                    new = false
                    i.updateCoords(cx,cy)
                    break
            if new:
                p = Car.MyCar(pid,cx,cy,max_p_age)
                cars.append(p)
                pid += 1
            cv2.circle(frame,(cx,cy),5,(0,0,255), -1)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.drawContours(frame,cnt,-1,(0,255,0),3)
    for i in cars:
        if len(i.getTrack()) >= 2:
            pts = np.array(i.getTrack(),np.int32)
            pts = pts.reshape((-1,1,2))
            frame = cv2.polylines(frame,[pts],False,i.getRGB())
        if i.getId() == 9:
            print(str(i.getX()),',',str(i.getY()))
        cv2.putText(frame,str(i.getId()),(i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)

    cv2.imshow('frame',frame)

    # abort and exit with Q or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()