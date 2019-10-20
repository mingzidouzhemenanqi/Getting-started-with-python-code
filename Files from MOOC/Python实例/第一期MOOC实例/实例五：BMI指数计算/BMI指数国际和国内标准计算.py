#BMI指数国际和国内标准计算

w,h=eval(input("请输入体重（KG）和身高（M），并用逗号隔开："))
b=w/pow(h,2)
#print("{:.2f},{:.2f}".format(w,h))
print("BMI指数为：{:.2f}".format(b))
nei=" "
ji=" "
if b<18.5:
    nei="偏瘦"
    ji="偏瘦"
elif 18.5<=b<=24:
    nei="正常"
    ji="正常"
elif 24<b<=25:
    nei="偏胖"
    ji="正常"
elif 25<b<=28:
    nei="偏胖"
    ji="偏胖"
elif 28<b<30:
    nei="肥胖"
    ji="偏胖"
else :
    nei="肥胖"
    ji="肥胖"
print("您的BMI指标：国际'{0}',国内'{0}'".format(ji,nei))






