#获取不定长度的用户数据

def getnumber():
    num=[]
    while True:
        i=input("请输入数据（空格退出）：")
        if i!=" ":
            num.append(eval(i))
        else :break
    return num
    
        
