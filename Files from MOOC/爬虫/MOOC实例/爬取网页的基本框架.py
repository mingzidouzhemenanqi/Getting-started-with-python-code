#爬取网页的通用代码框架

import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#如果状态不是200则抛出异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "ERROR"

if _name_=="_main_":
    url=input("请输入网址：")
    print(getHTMLText(url))
