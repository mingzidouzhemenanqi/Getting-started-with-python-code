import time
import os,shutil

usb = "E:/"
tofile = r'C:\Users\Forry\Desktop\1'
while True:
    if os.path.exists(usb):#判断U盘是否插入
        content = os.listdir(usb)#获取文件
        print(content)
        x=[i for i in content ]
        shutil.copy(os.path.join(usb,x[8]),tofile)#拷贝文件
        break
    else:
        time.sleep(3)


