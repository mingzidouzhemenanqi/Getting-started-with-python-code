#圆周率近似值计算1

import time as t
start=t.perf_counter()
pi=0
for k in range(10000):
    s=pow(1/16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
    pi+=s
end=t.perf_counter()
tt=end-start
print("圆周率近似值={}\n计算用时为{}".format(pi,tt))

