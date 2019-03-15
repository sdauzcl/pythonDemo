import time
print(time.time())
print(time.localtime())
print(time.localtime()[0],time.localtime().tm_mon)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1501245654)))
time1 = time.asctime(time.localtime(1501245654))
print(time1)


a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
b = "  hello world"
print(b.lstrip("aa"))

import calendar
print(calendar.calendar(2018))
print(calendar.month(2018,8,12))#12代表间隔距离
print(calendar.firstweekday())
print(calendar.isleap(1900))#返回是否是闰年
print(calendar.leapdays(2000,2018))
i = 0
for x in range(2000,2019):
    if calendar.isleap(x):
        i = i + 1
print(i)
for x in range(2):
    print(x)
print(calendar.monthrange(2018,2))