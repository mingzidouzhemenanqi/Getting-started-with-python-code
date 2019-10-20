#求中位数

def middlenum (sum1,i):
    sorted(sum1)
    if i/2 == 0:
        k=1/2*(sum1[i/2-1]+sum1[i/2])
    else :
        k=sum1[int(i/2)]
    return k
