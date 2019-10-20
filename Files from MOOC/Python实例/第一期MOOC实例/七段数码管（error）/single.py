#单个数码管绘制

import turtle as t

def dk():
    t.penup()
    t.fd(10)

def dl (l):
    if l==True:
       t.pendown()
    else :
       t.penup()
    t.fd(40)
    dk()
    t.right(90)
    dk()

def dn (n):
    dl(True) if n in [2,3,4,5,6,8,9] else dl(False)
    dl(True) if n in [0,1,3,4,5,6,7,8,9] else dl(False)
    dl(True) if n in [0,2,3,5,6,8,9] else dl(False)
    dl(True) if n in [0,2,6,8] else dl(False)
    t.fd(-10)
    t.left(90)
    t.fd(7)
    dl(True) if n in [0,4,5,6,8,9] else dl(False)
    dl(True) if n in [0,2,3,5,6,7,8,9] else dl(False)
    dl(True) if n in [0,1,2,3,4,7,8,9] else dl(False)
    t.left(180)
    t.penup()
    t.fd(60)
    








