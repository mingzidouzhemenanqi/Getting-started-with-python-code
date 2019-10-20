# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:51:27 2019

@author: Forry
"""

import sys, os

'''
定义合并函数，第一个参数是待合并文件路径，第二个是文件合并后存放路径,
第三个是合并后的文件名
'''
def joinfile(fromdir, todir, filename):
    #检测存放路径是否存在
    if not os.path.exists(todir):
        os.mkdir(todir)
    #检测待分割文件路径是否存在
    if not os.path.exists(fromdir):
        return '文件路径不存在'

    #用写二进制方式打开文件合并
    outfile = open(os.path.join(todir, filename), 'wb')
    #将待分割文件夹中所有文件存放入列表中
    files = os.listdir(fromdir)
    #将列表中的所有文件名进行排序
    files.sort()
    #遍历列表中所有文件
    
    for file in files:
        #拼接文件夹和文件名
        filepath = os.path.join(fromdir, file)
        #以二进制读的方式打开当前列表元素所表示的文件
        infile = open(filepath, 'rb')
        #读入该文件所有内容
        data = infile.read()
        #将当前文件写入合并文件
        outfile.write(data)
        #关闭当前子文件
        infile.close()
    #关闭合并文件
    outfile.close()

if __name__ == '__main__':
    #输入合并文件所需信息
    fromdir = input("请输入存放待合并文件的文件夹")
    todir = input("请输入存放合并后文件的文件夹")
    filename = input("请输入合并后文件的文件名")
    try:
        #调用合并函数
        joinfile(fromdir, todir, filename)
    except:
        #文件操作错误提示
        print("文件合并错误")
        print(sys.exc_info()[0], sys.exc_info()[1])
    else:
        #输入合并成功信息
        print("合并成功：", filename, "位于", todir)
    














