#网络图片爬取

import requests 
import os

url=input("请输入网址：")
root=input("请输入保存地址")
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
