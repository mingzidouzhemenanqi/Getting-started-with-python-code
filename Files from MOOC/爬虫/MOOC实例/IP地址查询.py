#IP地址查询

import requests

url="http://m.ip138.com/ip.asp?ip="
try:
    v=input("请输入要查询的地址")
    r=requests.get(url+v)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("ERROR")
    
