# encoding:utf-8
import os


def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            list_name.append(file_path)
        else:
            pass

listname = []
listdir('C:\\Users\\yyl\\Downloads\\Baidu Net Disk Downloads\\清华学霸尹成爬虫课件',listname)
# print(listname) # 获取文件夹路径成功

for dir in listname:
    try:
        os.remove(dir+"\\百度云SVIP长期免费使用.url")
        os.remove(dir + "\\本教程由我爱学it提供.url")
        os.remove(dir + "\\高清电子书籍.url")
        os.remove(dir + "\\更多精品教程.url")
        # os.remove(dir + "\\下载必看.txt")
    except:
        print(dir,"erro")
