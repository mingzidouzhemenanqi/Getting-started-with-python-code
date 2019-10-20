#import re
import requests
from bs4 import BeautifulSoup 
import bs4
import traceback
import pandas

def gethtml(url):
    try:
        tr=requests.get(url)
        tr.raise_for_status()
        tr.encoding="utf-8"
        return tr.text
    except:
        return ""

def analyzehtml(tr):
    try:
        if tr=="":
            return ""
        
        infolist={}
        soup=BeautifulSoup(tr,"html.parser")#解析页面信息
        stockinfo = soup.find('div',attrs={'class':'stock-bets'})#锁定信息位置
     
        #爬取股票名称
        name=stockinfo.find_all(attrs={'class':'bets-name'})[0]
        infolist.update({'股票名称':name.text.split()[0]})

        #爬取股票相关数据
        start=stockinfo.find_all('dt')
        end=stockinfo.find_all('dd')
        for j in range(len(start)):
            key=start[j].text
            value=end[j].text
            infolist[key]=value

        return infolist
    
    except:
        return ""

def writing(ta):
    fpath="C:\系统\BaiduStockInfo.txt"
    with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(ta) + '\n' )
                

def main():
    url1='https://gupiao.baidu.com/stock/'
    s=['sh601766','sh601989','sz002024']
    for i in range(3):
        try:
            url=url1+s[i]+'.html'
            tr=gethtml(url)
            ta={}
            ta=analyzehtml(tr)
            writing(ta)
        except:
           continue

main()



    

    
