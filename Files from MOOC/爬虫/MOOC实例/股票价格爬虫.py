import re
import requests
from bs4 import BeautifulSoup 
import bs4
import traceback

def gethtml(url,code="utf-8"):
    try:
        tr=requests.get(url)
        tr.raise_for_status()
        tr.encoding=code
        return tr.text
    except:
        return ""


def huoqumingcheng(lst,url):
    html=gethtml(url)
    print(html)
    soup=BeautifulSoup(html,"html.parser")
    a=soup.find_all('a')
    print(a)
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])#获取股票代码
        except:
            continue


def paquneirong(lst,url,fp):
    for k in range(3):
        i=lst[k]
        url1=url+i+".html"
        print(url1)
        html=gethtml(url1)
        try:
            if html=="":
                continue
            infolist={}
            soup=BeautifulSoup(html,"html.parser")#解析页面信息
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

            print(infolist)

            #输出爬取内容
            with open(fp,'a',encoding='utf-8') as f:
                f.write(str(infolist))
        except:
            continue

            
def main():
    url1= 'https://quote.eastmoney.com/stocklist.html'
    url2= 'https://gupiao.baidu.com/stock/'
    cunchu='C:/gupaishuju.txt'
    slist=['sh601766','sh601989','sz002024']
    #huoqumingcheng(slist,url1)
    paquneirong(slist,url2,cunchu)

main()




















    
    
