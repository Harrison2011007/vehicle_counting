import time
import xlwt
import xlrd
import openpyxl
import pandas as pd


# print(time.time())
io = r'E:\work2019\出租车数据\Taxi_GPS_2019_09_03.csv'
data = pd.read_csv(io)
fileread = open('E:\\work2019\\Mar\\images\\1.txt','r')

fileread.read()
# print(fileread)
fileread.close()

demo = open('E:\\work2019\\Mar\\images\\2.txt','w')
demo.write(str(fileread))
demo.close()
# data1 = []
# data1.append(data['Pos_time'].values)
#
# demo.write(str(data1))
# demo.close()

# print(data['Pos_time'].values)