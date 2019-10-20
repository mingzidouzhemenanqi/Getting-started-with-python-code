#主函数

import huizhi as h
import single as s
import time as ti
import turtle as t
import huoqu as hu

def main():
    t.setup(800,350)
    t.penup()
    t.fd(-300)
    x=input("若想绘制系统时间，输入1\n ,若想自行输入绘制时间，输入2：")
    if x=="1":
        list1=ti.strftime('%Y+%m-%d=',ti.gmtime())
        list2=list(list1)
        h.huizhi(list2)
    if x=="2":
        a=hu.huoqu()
        list3=list(a)
        h.huizhi(a)
    else:
        print("EROOR")
        

main()
        
