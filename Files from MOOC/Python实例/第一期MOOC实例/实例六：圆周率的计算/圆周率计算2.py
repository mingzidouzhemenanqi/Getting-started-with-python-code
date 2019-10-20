#圆周率计算2

import time as t
import random as r

zongshu=10000*10000
dianshu=0
start=t.perf_counter()
for i in range(zongshu):
    x,y=r.random(),r.random()
    s=pow(x*x+y*y,0.5)
    if s<1:
        dianshu+=1

pi=4*dianshu/zongshu
end=t.perf_counter()
tt=end-start
print("圆周率约为：{}\n计算用时：{}".format(pi,tt))
