#方差计算

def fc (num,ave,i):
    j=0.0
    for k in num:
        j+=(k-ave)**2
    return pow(j/i,0.5)
    
