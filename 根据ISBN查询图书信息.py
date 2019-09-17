from urllib import request
import json
isbn=215859
url ="http://119.29.3.47:9001/book/worm/isbn?isbn=" + str(isbn)

html = request.urlopen(url).read() # 抓取网页源码
html = str(html, encoding='utf-8') # 设置编码格式
# print(html) # 打印获取的信息
book_info = json.loads(html) # json数据转为字典
# print(type(book_info)) # 查看获得的数据类型
# print(book_info) # 打印字典

# 格式化打印图书信息
print("ISBN: ",book_info['data']['isbn'])
print("name: ",book_info['data']['name'])
print("title: ",book_info['data']['title'])
print("author: ",book_info['data']['author'])
print("publisher: ",book_info['data']['publisher'])
print("publishingTime: ",book_info['data']['publishingTime'])
print("folio: ",book_info['data']['folio'])
