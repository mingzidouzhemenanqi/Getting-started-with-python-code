from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

def getHTMLText(url):
        driver = webdriver.PhantomJS(executable_path='phantomjs')  # phantomjs的绝对路径
        time.sleep(2)
        driver.get(url)  # 获取网页
        time.sleep(2)
        return driver.page_source

url = 'https://www.enlightent.cn/research/rank/weiboSearchRank/'
a = getHTMLText(url)
print(a)
