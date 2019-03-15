import numpy as np

print(np.arange(0,1,0.2))
print(np.linspace(0,1,12))


c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print(c)
c.shape = 4,3
print(c)
c.shape = 2,-1
print(c)


a = np.arange(10)
print(a)
print(a[3:5])# 用范围作为下标获取数组的一个切片，包括a[3]不包括a[5]

b = range(10)
print(b)