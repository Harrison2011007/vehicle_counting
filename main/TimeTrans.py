import time
import xlwt
import xlrd
import openpyxl
import pandas as pd


# print(time.time())
io = r'J:\org_xy.csv'
data = pd.read_csv(io)

print(data['x'].values)

