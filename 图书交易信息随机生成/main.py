import random
import sqlite3


user_id_max = 1000

database_name = 'log'
conn = sqlite3.connect('orders.sqlite3') # 打开链接
c = conn.cursor()
conn_books = sqlite3.connect('D:\swProject\pyCharm\webDjango\db.sqlite3') # 图书信息源


get_sql = 'select title,tag from webapp_bookinfo'
books_info = conn_books.execute(get_sql) # sqllite

for book in books_info:
    user_id = random.randint(1,user_id_max) # 生成用户id
    book_title = book[0]
    book_kind = book[1]


    insert_sql = "INSERT INTO log(user_id,book_title,book_kind) VALUES ('%d','%s','%s')"%(user_id,book_title,book_kind)
    # insert_sql = 'INSERT INTO log(log_id,user_id,book_title,book_kind) VALUES ({},1,"活着","小说")'.format(log_id)
    c.execute(insert_sql) # sqllite
    conn.commit()# commit 语句执行，更改数据库
    print("插入图书--->", book_title)

conn.close() # 关闭链接
conn_books.close() # 关闭链接