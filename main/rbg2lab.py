from PIL import Image
import xlwt
import openpyxl
import pandas as pd
# 读取图片并获取每个像素的rgb值
imTree = Image.open('E:\\work2019\\Mar\\images\\1.jpg')
pix = imTree.load()
Twidth = imTree.size[0]#获取图片宽度
Theight = imTree.size[1]#获取图片长度
# print(Twidth)
imTree = imTree.convert('RGB')#获取rgb值
#建立一个序列，将rgb值存入其中
rgbarray = []
for x in range(Twidth):
    for y in range(Theight):
        r,g,b = imTree.getpixel((x,y))
        rgb = r,g,b
        rgbarray.append(rgb)
# 打印试一下对不对
# print(rgbarray)
# print(rgbarray[0])
# print(rgbarray[0][0])
# print(rgbarray[0][1])
# print(rgbarray[0][2])
# print(len(rgbarray))
# lab值的接收值
l = []
a = []
b = []
# rgb到lab转换公式如下：
# L = 0.2126007 * R + 0.7151947 * G + 0.0722046 * B;
# a = 0.3258962 * R - 0.4992596 * G + 0.1733409 * B + 128;
# b = 0.1218128 * R + 0.3785610 * G - 0.5003738 * B + 128;
for i in range(len(rgbarray)):
    l1 = int(0.2126007 * rgbarray[i][0] + 0.7151947 * rgbarray[i][1] + 0.0722046 * rgbarray[i][2])#l1,a1,b1是过渡值
    a1 = int(0.3258962 * rgbarray[i][0]  - 0.4992596 * rgbarray[i][1] + 0.1733409 * rgbarray[i][2] + 128)
    b1 = int(0.1218128 * rgbarray[i][0] + 0.3785610 * rgbarray[i][1] - 0.5003738 * rgbarray[i][2] + 128)
    l.append(l1)
    b.append(b1)
    a.append(a1)
# 试一下第一个值转化对不对
# print(l)
# l = 0.2126007 * rgbarray[0][0] + 0.7151947 * rgbarray[0][1] + 0.0722046 * rgbarray[0][2]
# a = 0.3258962 * rgbarray[0][0]  - 0.4992596 * rgbarray[0][1] + 0.1733409 * rgbarray[0][2] + 128
# b = 0.1218128 * rgbarray[0][0] + 0.3785610 * rgbarray[0][1] - 0.5003738 * rgbarray[0][2] + 128
# print(l)
# print(a)
# print(b)

lab = []
lab2 = {}
for i in range(len(l)):
    lab1 = l[i],a[i],b[i]#lab1是过渡值
    lab.append(lab1)
# 打印出lab值
print(lab)
print(len(l))
lab_sorted = sorted(lab)
# print(lab)#rgb到lab值转换完毕
print(lab_sorted)

# lst = list(set(lab_sorted))#过渡用的
setlst = set(lab_sorted)
# 将lab值存入到字典中
# d_lab = dict()
# print(d_lab)
print(setlst)
print(len(setlst))
# 写入到txt中
demo = open('E:\\work2019\\Mar\\images\\1.txt','w')
demo.write(str(lab))
demo.close()



# 写入到excel中
# Excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
# table = Excel.add_sheet('hello',cell_overwrite_ok=True)  #sheet名命名为hello
# i = 0
# for x in range(Twidth):
#      for y in range(Theight):
#         table.write(x,y,str(lab[i]))#写入到excel中write（row,col,data）
#         i = i+1
#
# Excel.save(r'E:\\work2019\\Mar\\images\\1.xls') #Excel表保存为world.xls
