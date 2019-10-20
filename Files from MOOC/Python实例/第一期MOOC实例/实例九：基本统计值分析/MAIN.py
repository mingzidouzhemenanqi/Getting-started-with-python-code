import huoqu
import qiuhe
import pingjun
import zhongwei
import fangcha

def main():
    num=[]
    num=huoqu.getnumber()
    k=len(num)
    sum1=qiuhe.sumnum(num)
    ave=pingjun.avenum(sum1,k)
    zw=zhongwei.middlenum(num,k)
    fc=fangcha.fc(num,ave,k)
    print("和：{}\n平均：{}\n方差：{:.2f}\n中位数：{}".format(sum1,ave,fc,zw))

main()
