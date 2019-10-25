import time

import psycopg2

conn = psycopg2.connect(database="trans", user="postgres", password="123456", host="127.0.0.1", port="5432")

print ("Opened database successfully")

timeStamp = 1570000000
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print (otherStyleTime)   # 2013--10--10 23:40:00