import cv2

import math
from PIL import Image
# imgBird = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG',cv2.IMREAD_COLOR)
# imgTree = cv2.imread('E:\\work2019\\Mar\\images\\DJI_0034.JPG',cv2.IMREAD_COLOR)
imgTree = Image.open('E:\\work2019\\Mar\\images\\car.jpg')

# 假设我们已经用ps拾取了所保护鸟类的所有颜色，获取颜色种类为18，每种颜色放在一个集合
# 鸟类的保护色命名为Pcolor1，Pcolor2，Pcolor3.....
# 树的颜色命名为Tcolor1，Tcolor2，Tcolor3....
#假设颜色总数为n = 18，则求 颜色总数的30%0


RGBpix = imgTree.load()
# print(RGBpix)
# PSize = imgTree.shape
# print(PSize)#获取图片尺寸
Pheight = imgTree.size[0] #获取图片高度
Pwidth = imgTree.size[1] #获取图片宽度
RGBarray = []
# [r, g, b] = RGBpix[x, y]
# rgb = [r, g, b]
# print(rgb)
demo = open('E:\\work2019\\Mar\\images\\rgb.txt','w')
for x in range(Pwidth):
    for y in range(Pheight):
        r, g, b = RGBpix[x,y]
        rgb = [r,g,b]
        print(rgb)
        RGBarray.append(rgb)
        demo.write(str(RGBarray))
# print(RGBarray)
demo.close()
# PSize = PSize.convert('RGB')
# demoLab = open('E:\\work2019\\Mar\\images\\rgb.txt','r')
# for x in range(Pwidth):
#     for y in range(Pheight):
#         demoLab.read(rgb)
#         print(rgb)
#LAB颜色分类与rgb颜色分类的转换
# void RGB2Lab2(double R, double G, double B, double &L, double &a, double &b)
# {
#       L = 0.2126007 * R + 0.7151947 * G + 0.0722046 * B;
#       a = 0.3258962 * R - 0.4992596 * G + 0.1733409 * B + 128;
#       b = 0.1218128 * R + 0.3785610 * G - 0.5003738 * B + 128;
# }
for i in range(len(RGBarray)):
    l[i] = 0.2126007 * RGBarray[i][0] + 0.7151947 * RGBarray[i][1] + 0.0722046 * RGBarray[i][2]
    a[i] = 0.3258962 * RGBarray[i][0]  - 0.4992596 * RGBarray[i][1] + 0.1733409 * RGBarray[i][2] + 128
    b[i] = 0.1218128 * RGBarray[i][0] + 0.3785610 * RGBarray[i][1] - 0.5003738 * RGBarray[i][2] + 128
    # l1 = 0.2126007 * RGBarray[1][0] + 0.7151947 * RGBarray[1][1] + 0.0722046 * RGBarray[1][2]
    # 强制取整数
    l = int(l[i])
    a = int(a[i])
    b = int(b[i])
print(l[1])





# Pcolor = []
# Tcolor = []
# n = 19
# color_in_use = int(round((n*0.3),0)) #前30%的颜色，命名为有用颜色
# # 输出一下，看结果对不对
# print(color_in_use)
# for i in range(0,color_in_use):
#     lab[i] = (pow((Pcolor[i].index(1)-Tcolor[i].index(1)),2)+pow((Pcolor[i].index(2)-Tcolor[i].index(2)),2)+pow((Pcolor[i].index(3)-Tcolor[i].index(3)),2))**0.5
#
#     if lab[i] <= 9.5:
#         print(lab[i])
#         print('this is ProtectTree!')
#     else:
#         continue





# cv2.imshow('imageBird',imgBird)
# cv2.imshow('imageTree',imgTree)
# cv2.waitKey(0)
# cv2.destroyAllWindows()