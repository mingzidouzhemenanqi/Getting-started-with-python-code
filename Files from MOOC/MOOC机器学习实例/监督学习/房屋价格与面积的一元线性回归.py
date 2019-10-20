# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:49:06 2019

@author: Forry
"""

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

#Store price data
datasets_y = []
#Storage area data
datasets_x = []
#open the file of data
fp = open('price.txt','r')
#read all data
lines = fp.readlines()
for line in lines:#Line by line
    item = line.strip().split(',')#Remove comma
    datasets_x.append(int(item[0]))
    datasets_y.append(int(item[1]))

#Calculate the total number of data
lengh = len(datasets_x)
#Convert datasets_x to a 2_dimensional array
datasets_x = np.array(datasets_x).reshape([lengh,1])
#Convert datasets_y to array
datasets_y = np.array(datasets_y)

#Establish the arithmetic progression with the maximum 
#and minimum values of datasets_x as the range
minx = min(datasets_x)
maxx = max(datasets_x)
x = np.arange(minx, maxx).reshape([-1, 1])

#Call the linear regression model, build the equation
linear = linear_model.LinearRegression()
#fit the data
linear.fit(datasets_x, datasets_y)

#draw data scatter
plt.scatter(datasets_x, datasets_y, color='red')
#draw the regression model
plt.plot(datasets_x, datasets_y, color='blue')
#draw the label
plt.xlabel('Area')
plt.ylabel('price')
plt.show()

 

    
    









