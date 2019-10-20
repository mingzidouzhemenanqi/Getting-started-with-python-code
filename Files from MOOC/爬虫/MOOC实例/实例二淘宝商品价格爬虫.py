#淘宝价格定向爬虫

import requests as rq
import re
import bs4
from bs4 import BeautifulSoup as be
import traceback

def gethtml(url):
    try:
        r=rq.get(url,timeout=30)
        a=r.raise_for_status()
        print(a)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
    

def prasepage(ilt,html):
    #try:
    a=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
    b=re.findall(r'\"raw_title\"\:\".*?\"',html)
    for i in range(len(a)):
        price=eval(a[i].split(':')[1])
        name=eval(b[i].split(':')[1])
        ilt.append([name,price])
    '''except:
        print("")'''

def printlist(ilt):
    moban="{:4}\t{:8}\t{:20}"
    print(moban.format("序号","商品","价格"))
    i = 0
    for k in ilt:
        i+=1
        print(moban.format(i,k[0],k[1]))
        

def main():
    goods=input("请输入要搜索的商品：")
    depth=input("请输入爬取页数")
    lianjie="https://s.taobao.com/search?q="+goods
    infolist=[]
    for i in range(int(depth)):
        try:
            url=lianjie+"&s="+str(44*i)
            html=gethtml(url)
            prasepage(infolist,html)

        except:
            continue
    printlist(infolist)

main()


















    
    
