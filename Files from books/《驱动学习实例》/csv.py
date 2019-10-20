# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:09:20 2019

@author: Forry
"""
'''
csv文件与Excel文件之间的转化
'''
import csv
import xlwt,xlrd
import sys,os


#csv文件转化为Excel文件
def CsvToExcel(csvfile, excelfile):
     if not os.path.exists(csvfile):
        #抛出错误提示
        return 'csv文件不存在'
     #新建工作簿
     
     myexcel = xlwt.Workbook()
     #新建表格，表格命名为mysheet
     mysheet = myexcel.add_sheet("mysheet")
     #用只读方式打开csv文件
     csvfile1 = open(csvfile,'r')
     #读取信息到reader对象中
     reader = csv.reader(csvfile1)
     #初始化行号
     row = 0
     #按行遍历数据
     for line in reader:
        #初始化列号
        col = 0
        #遍历每列元素
        for i in line:
            #把遍历到的元素写入Excel表格中对应的单元格
            mysheet.write(row, col, i)
            col += 1
        row += 1
     #保存文件
     mysheet.save(excelfile)
     #关闭文件
     csvfile.close()
     print('转换完成')

#Excel文件转化为csv文件
def ExcelToCsv(excelname, csvname)
    
    
    
















