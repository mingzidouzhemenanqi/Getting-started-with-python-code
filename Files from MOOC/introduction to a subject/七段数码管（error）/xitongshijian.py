#获取系统时间并返回对应字符串

import time as t

def gettime():
    b=t.strftime('%Y+%m-%d=',t.gmtime())
    return b
