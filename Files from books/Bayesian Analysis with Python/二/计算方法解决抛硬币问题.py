#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pymc3 as pm

np.random.seed(123)
n_experiment = 4
#预设真实参数
theta_real = 0.35 
#设置数据
data = stats.bernoulli.rvs(p=theta_real, size=n_experiment)
print(data)
data=np.array([1,0,0,0])

'''模型的描述'''
#构建模型容器
with pm.Model() as first_model: 
    theta = pm.Beta('theta', alpha=1, beta=1)
    y = pm.Bernoulli('y', p=theta, observed=data)
   
    '''推断'''
    #尝试返回最大后验
    start = pm.find_MAP()
    #定义采样方法
    step = pm.Metropolis()
    print(1)
    #进行推断          采样次数  采样方法  初始点
    trace = pm.sample(1000, step=step, start=start, cores=1)
'''收敛性测试
burnin = 10
chain = trace[burnin:]
pm.traceplot(chain, lines={'theta':theta_real})
'''

with first_model:
    step = pm.Metropolis()
    multi_trace = pm.sample(1000, step=step,njobs=4, cores=1)#njobs=4

burnin = 0
multi_chain = multi_trace[burnin:]
pm.traceplot(multi_chain, lines={'theta':theta_real})


# In[6]:


pm.gelman_rubin(multi_chain)


# In[7]:


pm.forestplot(multi_chain, varnames=['theta'])


# In[8]:


pm.summary(multi_chain)#


# In[11]:


pm.autocorrplot(multi_chain)#自相关


# In[12]:


pm.effective_n(multi_chain)['theta']#有效采样大小

