#按照要求绘制多个数码管

import single  as s
import turtle as t

def huizhi(s):
    for i in s:
        print("{}".format(i))
        if i=="+":
            t.write("年",font=("Arial",18,"normal"))
            t.pencolor("red")
            t.fd(40)
        elif i=="-":
            t.write("月",font=("Arial",18,"normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i=="=":
            t.write("日",font=("Arial",18,"normal"))
            t.pencolor("pink")
            t.fd(40)
        else:
            c=int(i)
            s.dn(c)
            
        

