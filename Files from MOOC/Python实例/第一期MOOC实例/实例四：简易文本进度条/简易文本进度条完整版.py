#简易文本进度条完整版

import time as t

jindu=50

print("STRAT".center(jindu//2,"-"))
s=t.perf_counter()
for i in range(jindu+1):
    a=i/jindu*100
    b=i*'*'
    c=(jindu-i)*'.'
    d=t.perf_counter()-s
    print("\r{:^3.0f}%:[{}->{}] {:.2f}s".format(a,b,c,d),end=" ")
    t.sleep(0.5)
print("\n"+"END".center(jindu//2,"-"))
