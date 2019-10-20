# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:17:20 2019

@author: Forry
"""

import numpy as np
from os import listdir
from sklearn import neighbors

#expand the matrix into acolumn of vectors
def loaddata(filename):
    remat = np.zeros([1024],int)
    #open the file
    fp = open(filename)
    #read all lines of the file
    lines = fp.readlines()
    #traverse all lines
    for i in range(32):
        for j in range(32):
            remat[i*32+j] = lines[i][j]
    return remat

#load the training data
def readdata(path):
    #get all the files under the floder
    filelist = listdir(path)
    #count the number of the files
    numfiles = len(filelist)
    #store all digital files
    datasets = np.zeros([numfiles, 1024],int)
    #store all corresponding labels
    #(different with nerual networks)
    hwlabels = np.zeros([numfiles])
    #traverse all files
    for i in range(numfiles):
        #get the name/path of files
        filepath = filelist[i]
        #get labels by the name of files
        digit = int(filepath.split('_')[0])
        #store the numbers
        hwlabels[i] = digit
        #read the files
        datasets[i] = readdata(path+'/'+filepath)
    return hwlabels, datasets

train_dataset, train_labels = readdata('trainingDigits')

#building the KNN classifier
knn = neighbors.KNeighborsClassifier(algorithm = 'kd_tree',
                                     n_neighbors=3)
knn.fit(train_dataset, train_labels)

#load test set
dataset, hwlabels = readdata('testDigits')

#predict and calculate the error rate
#predict
res = knn.predict(dataset)
#count the number of error
error_num = np.sum(res != hwlabels)
#count the number of test set
num = len(dataset)

print('Total num:',num,'Error num:',error_num,\
      'Error rate',error_num/float(num))














    
    
    