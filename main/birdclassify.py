import cv2
import math

imgBird = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG',cv2.IMREAD_COLOR)
imgTree = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG',cv2.IMREAD_COLOR)

# 假设我们已经用ps拾取了所保护鸟类的所有颜色，获取颜色种类为18，每种颜色放在一个集合
# 鸟类的保护色命名为Pcolor1，Pcolor2，Pcolor3.....
# 树的颜色命名为Tcolor1，Tcolor2，Tcolor3....
#假设颜色总数为n = 18，则求 颜色总数的30%
Pcolor = []
Tcolor = []
n = 19
color_in_use = int(round((n*0.3),0)) #前30%的颜色，命名为有用颜色
# 输出一下，看结果对不对
print(color_in_use)
for i in range(0,color_in_use):
    lab[i] = (pow((Pcolor[i].index(1)-Tcolor[i].index(1)),2)+pow((Pcolor[i].index(2)-Tcolor[i].index(2)),2)+pow((Pcolor[i].index(3)-Tcolor[i].index(3)),2))**0.5

    if lab[i] <= 9.5:
        print(lab[i])
        print('this is ProtectTree!')
    else:
        continue





cv2.imshow('imageBird',imgBird)
cv2.imshow('imageTree',imgTree)
cv2.waitKey(0)
cv2.destroyAllWindows()