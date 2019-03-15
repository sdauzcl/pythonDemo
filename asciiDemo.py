print(len('abc'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('你好好'.encode('utf-8')))

print('efg'.encode('ascii'))
str = '哈哈地'.encode('utf-8')
print(str)
print(str.decode('utf-8'))

print('%2f-%02d' % (3333.6743, 1))
print('%.2f' % 3.1415926)