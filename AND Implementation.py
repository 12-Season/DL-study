#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) #w1, w2 = 0.5 0.5
    b = -0.7
    
    temp = sum(x*w) + b
    
    if temp >= 0:
        return 1
    else:
        return 0


# In[6]:


AND(1, 0)
AND(1, 1)
AND(0, 1)
AND(0, 0)


# In[ ]:




