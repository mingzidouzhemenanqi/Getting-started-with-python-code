#百度关键词搜索代码

import requests

def getHTMLText(keyword):
    try:
        kv={'wd'+keyword}
        r=requests.get("http://www.baidu.com/s",params=kv)##error
        print("1")
        a=r.raise_for_status()#如果状态不是200则抛出异常
        print(a)
        r.encoding=r.apparent_encoding
        return (len(r.text))
    except:
        return "ERROR"

def main():
    keyword=input("请输入关键词：")
    print(getHTMLText(keyword))

main()
