# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 08:53:32 2019

@author: Forry
"""

import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
from scipy import stats
 
data = np.array([51.06, 55.12, 53.73, 50.24, 52.05, 56.40, 
                 48.45, 52.34, 55.65, 51.49, 51.86, 63.43, 
                 53.00, 56.09, 51.93, 52.31, 52.33, 57.48,  
                 57.44, 55.14, 53.93, 54.62, 56.09, 68.58, 
                 51.36, 55.47, 50.73, 51.94, 54.95, 50.39,
                 52.91, 51.5 , 52.68, 47.72, 49.73, 51.82, 
                 54.99, 52.84, 53.19, 54.52, 51.46, 53.73, 
                 51.61, 49.81, 52.42, 54.3 , 53.84, 53.16])

#模型设置
with pm.Model() as model_g:
    mu = pm.Uniform('mu', 40, 75)
    sigma = pm.HalfNormal('sigma', sd=10)
    y = pm.Normal('y', mu=mu, sd=sigma, observed=data)
    #对后验进行采样
    trace_g = pm.sample(1100,cores=1)

chain_g = trace_g[100:]
pm.traceplot(chain_g)





















