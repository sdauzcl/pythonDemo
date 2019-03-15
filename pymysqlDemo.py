import pymysql,sqlite3

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ccs_resource')
cursor = conn.cursor()
#cursor.execute("select * from test")

# 获取剩余结果的第一行数据
#row_1 = cursor.fetchall()
#print(row_1)
# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)

# 获取剩余结果所有数据
# row_3 = cursor.fetchall()
try:
    row_count=cursor.execute("select * from test1 where id=%s and num=%s",(1,2))
    row_1 = cursor.fetchone()
    print(row_1)
    print(row_1 == None)
except Exception as e:
    print(e)
try:
    print(1/0)
except Exception as e:
    print(e)
conn.commit()
cursor.close()
conn.close()

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,value)


