#!coding=utf-8
import requests
import re
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
import lxml


def doubanhudong(q, cat):  ###q  查询内容，cat 目录编号
    s = requests.session()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'Upgrade-Insecure-Requests': '1',
        'X-Requested-': 'XMLHttpRequest',
        # 'Referer': 'https://www.douban.com/search?cat={}&q={}'.format(cat,q),
        'Referer': 'https://www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36',
    }
    s.headers.update(headers)
    activity = []  ##频道名
    title = []  ##标题
    html = []  ##网址
    peoplenum = []  ##参加人数
    date = []  ##活动时间
    address1 = []  ##省
    address2 = []  ##城市
    address3 = []  ##详细地址
    abstract = []  ##概述
    for i in range(0, 100000, 20):
        url = 'https://www.douban.com/j/search?q={}&start={}&cat={}'.format(q, i, cat)
        req = s.get(url=url, verify=False)
        req = json.loads(req.text)

        # bs=BeautifulSoup(req,'lxml')
        # resultlist=bs.find_all(class_='result')
        bs = req['items']
        if bs == []:
            break

        for r in bs:
            print(r)
            i = BeautifulSoup(r, 'lxml')
            activity.append(i.find('span').get_text().strip())
            html.append(i.find('a')['href'].strip())
            title.append(i.find('a')['title'].strip())
            peoplenum.append(i.find(class_='info').get_text().strip().split('\n')[0])
            date.append(i.find(class_='info').get_text().strip().split('\n')[2].strip())
            address1.append(i.find(class_='info').get_text().strip().split('\n')[4].strip())
            address2.append(i.find(class_='info').get_text().strip().split('\n')[5].strip())
            address3.append(i.find(class_='info').get_text().strip().split('\n')[6].strip())
            try:
                abstract.append(i.find('p').get_text().strip())
            except:
                abstract.append('')

    # print(activity)
    # print(title)
    # print(html)
    # print(peoplenum)
    # print(date)
    # print(address1)
    # print(address2)
    # print(address3)
    # print(abstract)
    data = {
        'activity': activity, 'title': title, 'html': html, 'peoplenum': peoplenum, 'date': date, 'address1': address1,
        'address2': address2, 'address3': address3, 'abstract': abstract
    }
    df = pd.DataFrame(data)
    df.to_csv(r'./doubai.txt', index=False, encoding="utf-8")


if __name__ == '__main__':
    q = '电影'  ##搜索词
    cat = '1011'  ##频道编号
    doubanhudong(q, cat)