import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

def getHTMLText(url):
        driver = webdriver.PhantomJS(executable_path='phantomjs')  # phantomjs的绝对路径
        time.sleep(2)
        driver.get(url)  # 获取网页
        time.sleep(2)
        return driver.page_source

def fillUnivlist(html):
        soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
        tag = soup.find_all('div', attrs={'class': 'listInfo'})
        print(str(tag[0]))
        return 0

def main():
    url = 'http://sports.qq.com/articleList/rolls/' #要访问的网址
    html = getHTMLText(url) #获取HTML
    fillUnivlist(html)


main()














