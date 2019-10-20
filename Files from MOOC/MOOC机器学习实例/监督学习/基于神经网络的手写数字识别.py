# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:23:11 2019

@author: Forry
DBRHD数据集，由UCI机器学习中心提供
数据网址：https://archive.ics.uci.edu/mI/datasets/Pen-Based+Recognition+of+Handwritten+Digits
"""
import numpy as np
from os import listdir#open local file
from sklearn.neural_network import MLPClassifier

#load the data
def loaddata (filename):
    #define the return matrix
    matrix = np.zeros([1024],int)
    #open the file
    fp = open(filename)
    #read all lines of the file
    lines = fp.readlines()
    #traverse all lines of the file
    for i in range(32):
        for j in range(32):
            matrix[i*32+j] = lines[i][j]
    return matrix

def readdatasets(path):
    #get all the file under the folder
    filelist = listdir(path)
    #get the number of the file
    numfile = len(filelist)
    #store all digital file
    datasets = np.zeros([numfile,2014],int)
    #store all corresponding labels
    hwlabels = np.zeros([numfile,10])
    #traverse all file
    for i in range(numfile):
        #get the name/path of the file
        filepath = filelist[i]
        #get the label through the name of file
        digit = int(filepath.split('_')[0])
        #assign the corresponding labels to 1
        hwlabels[i][digit] = 1.0 
        #read the file
        datasets[i] = loaddata(path+'/'+filepath)
    return datasets,hwlabels

train_datasets, train_hwlabels = readdatasets('trainingDigits')

clf = MLPClassifier(hidden_layer_sizes=(100,),#a hidden layer containing 100 neurons
                    activation='logistic', solver='adam',
                    learning_rate_init=0.0001,#initial learning efficiency
                    max_iter=2000)#number of times

#function fit can automatically set the number of neurons
clf.fit(train_datasets, train_hwlabels)
            
#evaluation test set
datasets, hwlabels = readdatasets('testdigits')

#predict and calculation error rate
#predict
res = clf.predict(datasets)
#count the number of predicted error
error = 0
#the number of the test set
num = len(datasets)
#traverse the prediction results
for i in range(num):
    #比较长度为10的数组，，返回包含0,1的数组，0不同，1相同
    #若预测结果与实际相同，则全为1，否则不全为1
    if np.sum(res[i] == hwlabels[i]) < 10:
        error += 1

print('Total num:',num,'Wrong num:',error,\
      'Wrong Rate:' ,error/float(num))

















