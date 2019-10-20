#工作日的力量

def ddu():
    i=1.0
    for j in range(365):
        if j%7 in [0,6]:
            i=i*0.99
        else:
            i*=1.01
    return i

k=ddu()
print("工作日的力量:{:.3f}".format(k))        
         
