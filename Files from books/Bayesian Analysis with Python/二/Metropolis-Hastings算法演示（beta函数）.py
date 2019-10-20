# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:22:12 2019

@author: Forry
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def metropolis(func, steps=10000):
    #初始化
    sample = np.zeros(steps)
    old_x = func.mean()
    old_prob = func.pdf(old_x)
    a, b = 0, 0
    for i in range(steps):
        new_x = old_x + np.random.normal(0, 0.5)
        new_prob = func.pdf(new_x)
        acceptance = new_prob/old_prob
        if acceptance >= np.random.random():
            sample[i] = new_x
            old_x = new_x
            old_prob = new_prob
            a = a+1
        else:
            sample[i] = old_x
            b = b+1
    
    print('接受的个数：', a)
    print('拒绝的个数：', b)
    return sample

func = stats.beta(0.4, 2)
samples = metropolis(func=func)
x = np.linspace(0.01, .99, 100)
y = func.pdf(x)
plt.xlim(0, 1)
plt.plot(x, y, 'r-', lw=3, label='True distribution')
plt.hist(samples, bins=30, normed= True, label='Estimated distribution')
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$pdf(x)$', fontsize=16)
plt.legend(fontsize=16)












        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        