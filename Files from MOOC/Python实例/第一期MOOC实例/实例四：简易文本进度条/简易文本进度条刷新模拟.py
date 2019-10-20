#简易文本进度条刷新模拟

import time as t

jindu=10

for i in range(jindu+1):
    a=i*'*'
    b=(jindu-i)*'.'
    c=i*10
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end=" ")
    t.sleep(1)
