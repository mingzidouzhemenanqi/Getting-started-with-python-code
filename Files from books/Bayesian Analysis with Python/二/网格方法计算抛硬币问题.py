# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:54:13 2019

@author: Forry
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def yingbi(grid_point=100, heads=6, tosses=9):
    
    grid = np.linspace(0, 1, grid_point)
    prior = np.repeat(5, grid_point)
    likelihood = stats.binom.pmf(heads, tosses, grid)
    unstd_posterior = likelihood * prior
    posterior = unstd_posterior / unstd_posterior.sum()
    return grid, posterior

points = 15
h, n = 1, 4 #正面朝上次数和总次数
grid, posterior = yingbi(points, h, n)
plt.plot(grid, posterior, 'o-', label='heads = {}\ntosses = {}'.format(h, n))
plt.xlabel(r'$\theta$')
plt.legend(loc=0)
plt.show()










