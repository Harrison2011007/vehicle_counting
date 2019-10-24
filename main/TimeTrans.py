import time
import xlwt
import xlrd
import openpyxl
import pandas as pd


# print(time.time())
io = r'E:\work2019\出租车数据\Taxi_GPS_2019_09_03.csv'
data = pd.read_csv(io)

print(data.iloc[1:,2])

