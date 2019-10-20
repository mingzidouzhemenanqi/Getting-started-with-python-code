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

def fenxi(html):
       blist=[]
       soup = BeautifulSoup(html, 'html.parser')
       tag= soup.find('tbody')#定位JS生成数据部分
       b=tag.find_all('td')#将数据连同标签形成一个列表
       k=0
       for i in range(int(len(b)/9)):#按行划分
               alist=[]
               for j in range(9):
                       alist.append(b[k].text.split()[0])#单行逐个提取数据加入列表
                       k=k+1
               blist.append(alist)
       return blist





def main():
   
    '''
    #单页测试代码
    url1 = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E6%A1%82%E6%9E%97&month=201608'#城市名必须为二进制形式
    blist=[]
    html = getHTMLText(url1) #获取HTML
    print(html)
    blist.extend(fenxi(html))
    df=pd.DataFrame(blist)#将一年的数据形成DataFrame类型，可修改缩进
    df.to_excel('1.xlsx')#输出至源文件当前路径
    '''
    url1 = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E6%A1%82%E6%9E%97&month=' #爬取地址
    for i in range(2014,2018) :
            blist=[]
            #形成日期链接
            for j in range(1,13):
                f='0'+str(j) if j<=9 else str(j)
                url=url1+str(i)+f
                print(url)#输出当前爬取网址，作为进度条使用，可删除或修改
                html = getHTMLText(url) #获取HTML
                blist.extend(fenxi(html))#将上一句返回的列表加入blist
            df=pd.DataFrame(blist)#将一年的数据形成DataFrame类型，可修改缩进
            k=str(i)+'.xlsx'#形成文件名，但此句只包含时间
            df.to_excel(k)#输出至源文件当前路径

main()
