try:
    l=map(int,'1234g')
    for i in l:
        print(type(i))
        print(i)
except Exception as e:
    print(e)

print(123)

l2=filter(lambda x:x%2==0,[1,4,3,5,8])

print(list(l2))
# for i  in l2:
#     print(i)
#
# list = [1,4,6,7,-3,-10,7.8]
# print(sorted(list,key = lambda x:abs(x)))

foo = [1, 2, 3]
print(list(filter(lambda x:x%3 == 0,foo)))
