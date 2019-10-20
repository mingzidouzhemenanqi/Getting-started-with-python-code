# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:06:55 2019

@author: Forry
"""

import matplotlib.pyplot as plt#data visualization
#load the algorithm of PCA
from sklearn.decomposition import PCA 
#load the data of iris
from sklearn.datasets import load_iris

#加载和降维数据
data = load_iris()#以字典形式加载数据
#y表示数据集中的标签
y = data.target
#x表示数据集中的属性
x = data.data
#load the algorithm of PCA,降维后主成分位数目为2
pca = PCA(n_components=2)
#对原始数据进行降维，保存在reduced_x中
reduced_x = pca.fit_transform(x)

#按类别对降维后的数据进行保存
red_x, red_y = [], []#First type of data point
blue_x, blue_y=[], []#Second type of data point
green_x, green_y=[], []#Third type of data point

#按照iris类别将降维后的数据保存在不同列表中
for i in range(len(reduced_x)):
    if y[i] == 0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])

#数据可视化
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g',marker='.')
plt.show()










