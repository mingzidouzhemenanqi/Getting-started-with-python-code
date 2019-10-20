#体育竞技分析：

import random as r
def monibisai(an,bn,n):
    aj,bj=0,0
    for i in range(n):
        jieguo=danju(an,bn,i)
        if jieguo=='a':
            aj+=1
        else:
            bj+=1
    return aj,bj

def danju(an,bn,n):
    af,bf=0,0
    #qiu=faqiu(n)
    qiu='A'
    while  (af<=15 and bf<=15):
        if qiu=='A':
            if r.random()<an:
                af+=1
            else:
                qiu='B'
        else:
            if r.random()<bn:
                bf+=1
            else:
                qiu='A'
    if af>bf:
        return 'a'
    else:
        return 'b'

def jieshu(af,bf):
    return (af<=15 and bf<=15)

def faqiu(n):
    if n%2==0:
        return 'A'
    else :
        return 'B'

def fenxi(aj,bj,n):
    print("A的胜率为{},B的胜率为{}".format(aj/n,bj/n))

def huoqu():
    print("该程序用于简易模拟分析A,B两个球员的胜率")
    a=eval(input("请输入A的能力值（0,1）："))
    b=eval(input("请输入B的能力值（0,1）："))
    n=eval(input("请输入模拟局数："))
    return a,b,n

def main():
    a,b,n=huoqu()
    aj,bj=monibisai(a,b,n)
    fenxi(aj,bj,n)

main()

















    
            
        
    
