# 将加密分享的文件保存到自己云盘的目录下[2000g]

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import logging

# 设置日志
logging.basicConfig(filename="new.log",level=logging.ERROR)

# 有界面的就简单了
def ChromeDriverBrowser():
    driverChrome = webdriver.Chrome("./tools/chromedriver.exe")
    return driverChrome

# 登录云盘
def login(driver, username, password):
    orgin_url = 'https://pan.baidu.com/'
    driver.get(orgin_url)
    """
    # time.sleep(5)
    # elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    # elem_static.click()
    # time.sleep(0.5)
    # elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    # elem_username.clear()
    # elem_username.send_keys(username)
    # elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    # elem_userpas.clear()
    # elem_userpas.send_keys(password)
    # elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    # elem_submit.click()
    # 人工登录操作
    """
    print("此处需要人工操作，绕过验证：等待1分钟")
    time.sleep(60)


# 将加密分享的文件保存到自己云盘的目录下[2000g]
def extract(driver,line_num, srcurl, srcpwd):
    driver.get(srcurl)
    try:
        getpwd = driver.find_element_by_id("mkco9Kb")
        getpwd.send_keys(srcpwd)
        getButton = driver.find_element_by_link_text("提取文件")
        getButton.click()
        time.sleep(10)
        # 目前有两种情况
        # 一：分享文件是一压缩包
        # 二：分享的是一路径
        try:
            # 全选（情况二）
            selectall = driver.find_element_by_class_name("zbyDdwb")
            selectall.click()
        except NoSuchElementException:
            logging.debug("压缩包,不是文件夹link: " + srcurl + " : " + srcpwd)
            file_name = "log_img/zip/"+line_num+"-"+srcpwd+"_not_dirs.png"
            driver.save_screenshot(file_name)
            pass
        # 情况二 + 情况一
        savetodisk = driver.find_element_by_link_text("保存到网盘")
        savetodisk.click()
        time.sleep(5)
        # 2000g 保存路径
        selectdir = driver.find_element_by_xpath("//span[@node-path='/2000g']")
        selectdir.click()
        enter = driver.find_element_by_link_text("确定")
        enter.click()
        time.sleep(2)
    except NoSuchElementException:
        logging.error("找不到文件,提取失败link: "+srcurl+" : "+srcpwd)
        file_name = "log_img/"+line_num+"-"+srcpwd+"_no_file.png"
        driver.save_screenshot(file_name)
        pass


# 从txt中读取分享链接和提取密码
def read_txt():
    with open("hrefs", encoding="utf-8") as f:
        listUrl = f.readlines()
    with open("pws", encoding="utf-8") as f2:
        listpwd = f2.readlines()
    for i in range(len(listUrl)):
        listUrl[i] = listUrl[i].strip()
        listpwd[i] = listpwd[i].strip()
    return listUrl, listpwd


# 调用执行
def doWork():
    listUrl, listpwd = read_txt()
    driver = ChromeDriverBrowser()
    login(driver,"uername","password")
    for index in range(len(listUrl)):
        line_num = str(index + 1)
        srcurl = listUrl[index]
        srcpwd = listpwd[index]
        extract(driver,line_num, srcurl, srcpwd)
    driver.quit()


if __name__ == '__main__':
    doWork()



