# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:39:45 2019

@author: Forry
"""

'''文件分割程序'''

import sys,os

kb = 1024
mb = 1000*kb


#分割函数，第一个参数是待分割文件，第二个参数是分割后文件存放位置
#返回文件分割后的数目

def split(fromfile, todir, chunksize):
    #检查待分割文件是否存在
    if not os.path.exists(fromfile):
        #抛出错误提示
        return '该文件不存在'
    #检查分割后文件存放路径是否存在
    if not os.path.exists(todir):
        #不存在则创建该路径
        os.mkdir(todir)
        #存在则提示，是删除路径下所有文件还是重新选择路径
    else:
        print("该路径已存在，路径下可能存在文件，输入1覆盖该路径文件，输入2重新选择路径")
        s = int(input())
        if s == 1:
            for fname in os.listdir(todir):
                os.remove(os.path.join(todir,fname))
        else:
           return '重新输入路径'
    #分割初始标号
    print(1)
    partnum = 0
    #二进制格式打开文件
    f = open(fromfile,'rb')
    #文件大小不确定，采用无限循环结构
    while True:
        #依照分割大小读取子块
        chunk = f.read(chunksize)
        #循环结束条件
        if not chunk:
            break
        #块编号+1
        partnum += 1
        #构造文件名，并与目标文件拼接
        #文件命名方式：原文件名+part+块编号
        filename = os.path.join(todir,
                                (fromfile+'part%04d'%partnum))
        #以二进制方式写入文件
        fileobj = open(filename, 'wb')
        #当前的分块写入文件
        fileobj.write(chunk)
        #关闭文件
        fileobj.close()
    return partnum

if __name__ == '__main__':
    #输入文件分割所需的信息
    fromfile = input("请输入待分割的文件名")
    todir = input("请输入存储的文件路径")
    chunsize = int(input("请输入分割大小（以字节为单位）"))
    #获取绝对路径
    absfrom, absto = map(os.path.abspath,[fromfile,todir])
    print('分割文件',absfrom,'到',absto,'单个文件大小为',chunsize)
    try:
        #调用分割函数
        parts = split(fromfile, todir, chunsize)
    except:
        #文件操作错误提示
        print('分割错误：')
        print(sys.exc_info()[0], sys.exc_info()[1])
    else:
        if type(parts)==int:
            #显示分割成功信息
            print("分割成功：",parts,"个文件，位于",absto)
        else:
            print(parts)

        
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    