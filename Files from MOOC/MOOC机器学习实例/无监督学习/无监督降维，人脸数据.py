# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


"""

import matplotlib.pyplot as plt
#数据可视化
from sklearn import decomposition
#加载PAC算法包
from sklearn.datasets import fetch_olivetti_faces
#加载Olivetti人脸数据集导入函数
from numpy.random import RandomState
#加载RandomState用于创建随机种子

n_row , n_col = 2, 3
#设置图像展示时的排列情况为两行三列
n_components = n_row * n_col
#设置提取的特征的数目
image_shape = (64, 64)
#设置人脸数据图片的大小
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data#加载数据并打乱顺序
#设置图像展示方式
def plot_gallery(title, images, n_row=n_row, n_col=n_col):
    plt.figure(figsize=(2.*n_col, 2.26*n_row))
    #创建图片，并指定图片大小（英寸）
    plt.suptitle(title, size=16)
    #设置标题以及字号
    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i+1)#选择画制的子图
        vmax = max(comp.max(), -comp.min())
        
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray, 
                   interpolation='nearest', 
                   vmin= -vmax, vmax=vmax)
        #对数值进行归一化，并以灰度图显示
        plt.xticks(())
        plt.yticks(())
        #去除子图的坐标轴标签
    
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.93, 0.04, 0.)
    #调整子图的位置和间隔

#创建特征提取对象NMF，使用PCA进行对比.将其存放在一个列表中
estimators = [
        ('Eigenfaces - PCA using randomized SVD',
         decomposition.PCA(n_components=6,whiten=True)),
         #PCA的实例化
         ('Non-negative components - NMf',
          decomposition.NMF(n_components=6, init='nndsvda',
                            tol=5e-3))]
         #NMF的实例化
         
#降维后数据点的可视化
for name, estimator in estimators:#分别调用PCA和NMF
    estimator.fit(faces)#调用PCA或者NMF提取特征
    components_= estimator.components_#获取提取特征
    plot_gallery(name, components_[:n_components])
    #按固定格式进行排序

#可视化
plt.show()

    
    
         


        












