#定向爬虫，中国大学排名
import requests
import bs4
from bs4 import BeautifulSoup as be


def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding()
        return r.text
    except:
        return  ""
    
def fillunivlist(ulist,html):
    soup=be(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
            
def printlist(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
         print(tplt.format(ulist[0],ulist[1],ulist[2],chr(12288)))
        


def main():
    unifo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=gethtmltext(url)
    fillunivlist(unifo,html)
    printlist(unifo,20)

main()
