import time

import psycopg2

connect = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
db = connect.cursor()
sql = "SELECT update_tim FROM binhai_taxi_0903"
db.execute(sql)
result = db.fetchall()
# print(result[1])
# print(list(result[1]))
lstresult = []#用于将原来的数据变为list
for i in range(len(result)):
    lstresult.append(list(result[i]))
    # print(result[i])
# 将元素从列表中取出

print(lstresult[1][0])
demo = open('D:\\Program Files (x86)\\1.txt','w')
demo.write(str(lstresult))
demo.close()

print ("Opened database successfully")

timeStamp = int(lstresult[1][0])
timeStamp1 = timeStamp/1000
timeArray = time.localtime(timeStamp1)
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print (otherStyleTime)   # 2013--10--10 23:40:00
