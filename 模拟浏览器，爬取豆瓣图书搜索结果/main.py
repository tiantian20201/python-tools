from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pymysql
import re

# 连接数据库
connect = pymysql.connect(
    # localhost连接的是本地数据库
    host='localhost',
    # mysql数据库的端口号
    port=3306,
    # 数据库的用户名
    user='test',
    # 本地数据库密码
    passwd='123456',
    # 表名
    db='books',
    # 编码格式
    charset='utf8'
)
print("连接数据库成功！")
# 2. 创建一个游标cursor, 是用来操作表。
cursor = connect.cursor()


starturl = 'https://book.douban.com/'

driver = webdriver.Chrome("./chromedriver.exe")# 设置driver 模拟浏览器
wait = WebDriverWait(driver,10)# 设置等待时间为10s，超时则会报错
driver.get(starturl) # 打开网址
books = ['我的大学','老人与海']# 要搜索的内容列表


# 搜索函数,循环搜索
def search(i):
    while i >= 0:
        input = driver.find_element_by_xpath('//*[@id="inp-query"]')# 获取输入框
        submit = driver.find_element_by_xpath('//*[@id="db-nav-book"]/div[1]/div/div[2]/form/fieldset/div[2]/input')# 获取【搜索】按钮
        print('搜索图书【{}】...'.format(books[i]))# 打印提示
        input.clear()# 清空输入框
        input.send_keys('{}'.format(books[i]))# 输入搜索内容
        submit.click()# 模拟鼠标点击
        yield driver.page_source # 返回数据
        i -= 1 # 书籍游标-1

# 使用xpath获取一个图书页面的图书信息
def getBookInfo(href):
    # htmlfile = open('./1.html', 'r', encoding='utf-8') # 打开本地文件
    driver.get(href)
    soup = BeautifulSoup(driver.page_source, 'lxml')  # 创建CSS选择器
    info = soup.select_one('#info')  # css选择器匹配符合条件
    str_info = ''
    for child in info.children:
        if (child.string != None):
            str_info += str(child.string.strip())+";"
    info_list = str_info.split(';')
    for i in range(info_list.count('')): # 获取列表中的''项
        info_list.remove('') # 删除列表中的''项

    str_re = str(info_list)
    # htmlfile.close()# 关闭本地文件

    author = re.findall(r"作者:', '(.+?)'", str_re)[0]  # 获取信息---作者
    # print(author)
    publish = re.findall(r"出版社:', '(.+?)'", str_re)[0]  # 获取信息---出版社
    publish_year = re.findall(r"出版年:', '(.+?)'", str_re)[0]  # 获取信息---出版年
    price = re.findall(r"定价:', '(.+?)'", str_re)[0]  # 获取信息---定价
    isbn = re.findall(r"ISBN:', '(.+?)'", str_re)[0]  # 获取信息---ISBN

    title = soup.select_one('#wrapper > h1 > span')
    title = title.get_text()  # 获取信息---评分
    # print(title)
    score = soup.select_one('#interest_sectl > div > div.rating_self.clearfix > strong')
    score = score.get_text()  # 获取信息---评分
    # print(score.get_text())
    description = soup.select_one('#link-report > div:nth-child(1) > div > p:nth-child(1)')
    if description is not None:
        description = description.get_text()  # 获取信息---简介
    # print(description.get_text())
    img = soup.select_one('#mainpic > a > img')
    img = img['src']
    # print(img)
    # print(isbn,title,author,publish,publish_year,score,price,description,img)
    save_to_db(isbn,title,author,publish,publish_year,score,price,description,img) # 存储信息到数据库

#存储book信息到数据库
def save_to_db(isbn,title,author,publish,publish_year,score,price,description,img):
    print("插入图书【%s】数据..."%(title))
    insert_sql = "INSERT INTO book_info(isbn,title,author,publish,publish_year,score,price,description,img) " \
                 "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % (isbn,title,author,publish,publish_year,score,price,description,img)
    cursor.execute(insert_sql)
    print('图书【{}】信息存储完成！'.format(title))  # 打印提示
    # 4. 提交操作
    connect.commit()

# 定义主程序
def main():
    count=len(books)
    for result in search(len(books)-1): # 获取yield返回结果
        count -= 1 # 正在检索位置信息
        # 写入文件
        # with open(str(count)+".html","w",encoding="utf-8") as f:
        #     f.write(result)
        soup = BeautifulSoup(result,'lxml') # 创建CSS选择器
        hrefs = soup.select_one('a[href*="https://book.douban.com/subject/"][class="title-text"]') # css选择器匹配符合条件的hrefs
        # print(len(hrefs)) # 打印获取的hrefs
        print(hrefs['href'])  # 打印获取的链接
        getBookInfo(hrefs['href'])  # 进入链接，爬去格式化图书信息

        # 严格检查书名一致
        # for href in hrefs: # 遍历hrefs
        #     if (href.get_text()== books[count]): # 只需获取一个符合条件的href
        #         print(href['href']) # 打印获取的链接
        #         getBookInfo(href['href']) # 进入链接，爬去格式化图书信息
        #         print('图书【{}】信息存储完成！'.format(books[count]))# 打印提示
        #         break
        #     else:
        #         pass



if __name__ == '__main__':
    main()
    # 关闭数据库连接
    cursor.close()
    connect.close()
