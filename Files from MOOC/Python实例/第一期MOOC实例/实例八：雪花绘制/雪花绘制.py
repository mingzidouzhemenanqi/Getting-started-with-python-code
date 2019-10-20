#雪花绘制

import turtle as t
def snow(size,n):
    if n==0:
        t.fd(size)
    else :
        for i in [0,60,-120,60]:
            t.left(i)
            snow(size/3,n-1)

def main():
    t.setup(800,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pencolor("red")
    snow(300,3)
    for i in range(2):
        t.right(120)
        snow(300,3)
    t.done()


main()
