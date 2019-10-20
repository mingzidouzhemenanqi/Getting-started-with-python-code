# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 23:12:36 2019

@author: Forry
"""

import matplotlib.pyplot as plt
import numpy as np

n = 10000000

x, y = np.random.uniform(-1, 1, size=(2, n))
inside = (x**2 + y**2) <= 1
pi = inside.sum()*4/n
error = abs((pi-np.pi)/pi)*100

outside = np.invert(inside)

plt.plot(x[inside], y[inside], 'b.')
plt.plot(x[outside], y[outside], 'r.')
plt.plot(0, 0, label='$\hat \pi$ = {:4.9f}\nerror = {:4.3f}%'.format(pi, error), alpha=0)
plt.axis('square')
plt.legend(frameon=True, framealpha=0.9, fontsize=16)
plt.show()



















