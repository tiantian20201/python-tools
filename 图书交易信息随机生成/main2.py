import random
import sqlite3

user_id_max = 100

COUNT = 1

database_name = 'shares'
conn = sqlite3.connect('orders.sqlite3') # 打开链接
c = conn.cursor()

for i in range(20000):
    i += 1
    user_id = random.randint(1,user_id_max) # 生成用户id
    the_book_id = random.randint(1,2000)
    pre = random.randint(1,4)
    str_time = "%s-%s-%s %s:%s:%s"%(random.randint(2015,2019),random.randint(1,12),random.randint(1,28),
                                          random.randint(0,23),random.randint(1,60),random.randint(1,60))
    # print(str_time)
    # print(type(user_id),user_id)
    # print(type(the_book_id),the_book_id)
    # print(type(pre),pre)
    # print(type(str_time),str_time)
    insert_sql = "INSERT INTO shares(uid,iid,pre,time) VALUES('%d','%d','%d','%s')"%(user_id,the_book_id,pre,str_time)
    # insert_sql = "INSERT INTO shares(uid,iid,pre,times) VALUES(1,2,3,'2019-8-17 23:12:30')"
    c.execute(insert_sql) # sqllite
    conn.commit()# commit 语句执行，更改数据库
    print(COUNT)
    COUNT += 1

conn.close() # 关闭链接