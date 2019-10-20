#工作日的努力要达到多少程度才能赶上每天工作


def cs(up):
    k=1
    for i in range(365):
        if i%7 in [0,6]:
            k*=0.99
        else:
            k*=1+up
    return k

j=pow(1.01,365)

up=0.01
while 1:
    if cs(up)<j:
        up+=0.001
        continue
    else:
        print("每天的效率为：{:.3f}".format(up))
        break

'''improve

while cs(up)<j:
    up+=0.001
print("每天的效率为：{:.3f}".format(up))
'''





















    

            
    
