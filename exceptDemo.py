import time,logging
time = time.strftime('%Y-%m-%d %H:%M:%S')
a=10
b=0
try:
    print(a/b)
except BaseException as e:
    print('error',e)
finally:
    print("always excute")
print(123)

try:
    f = open('d:/aa.txt')#w+每次都清空
    f.write(time)
except BaseException as e:
    print('no file',e)
    #logging.exception(e)


# with open('b.txt') as f:
#     f.write(time)

print(123)
logging.info("2121")

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
print(666)