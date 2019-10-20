# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:28:33 2019

@author: Forry
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

datasets_x = []
datasets_y = []
fp = open('prices.txt', 'r')
lines = fp.readlines()
for line in lines:
    items = line.strip().split(',')
    datasets_x.append(int(items[0]))
    datasets_y.append(int(items[1]))
length = len(datasets_x)

datasets_x = np.array(datasets_x).reshape([length,1])
datasets_y = np.array(datasets_y)

minx = min(datasets_x)
maxx = max(datasets_x)
x = np.arange(minx,maxx).reshape([-1,1])

#Establish the quadratic polynomial feature of x
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(datasets_x)
#Learn the mapping between x_poly and datasets_y
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(x_poly, datasets_y)

#show the data
plt.scatter(datasets_x, datasets_y, color='red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)),
         color='blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    