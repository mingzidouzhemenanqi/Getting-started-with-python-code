#利用数据自动绘制轨迹

import turtle as t

t.title("自动绘制轨迹")
t.setup(800,600)
t.pencolor("red")
t.pensize(7)

#读取数据
d=[]
f=open("data.txt")
for line in f:
    line = line.replace("\n"," ")
    d.append(list(map(eval,line.split(","))))
f.close()

#绘制图形

for i in range(len(d)):
    t.pencolor(d[i][3],d[i][4],d[i][5])
    t.fd(d[i][0])
    if d[i][1] :
        t.right(d[i][2])
    else:
        t.left(d[i][2])









        
