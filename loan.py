# A = 10000
# b = 0.00345#4.9/(100*12)
# m = 12
A = 430000
b = 4.9/(100*12)
m = 360
month = round(A*b*pow(1+b,m)/(pow(1+b,m) - 1),2)
print(b,month)
ben = S = 0 #S 各个月的本金之和
for x in range(1,m+1):
    li = (A - S)*b
    ben = month - li
    S = S + ben
    #print(x,round(ben,2),round(li,2),round(li,2)+round(ben,2))

ben = S = 0 #S 各个月的本金之和
for x in range(1,m+1):
    li = (A - S)*b
    ben = A/m
    S = S + ben
    print(str(x) + '期',ben,li,round(ben,2),round(li,2),round(ben,2) + round(li,2))