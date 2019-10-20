#修改爬虫头部信息模拟浏览器代码框架

import requests

def getHTMLText(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url)#,header=kv)
        print("a")
        r.raise_for_status()#如果状态不是200则抛出异常
        r.encoding=r.apparent_encoding
        return (r.text)
    except:
        return "ERROR"

def main():
    url=input("请输入网址：")
    print(getHTMLText(url))

main()
