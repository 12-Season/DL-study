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


# In[7]:


def NAND(x1, x2):
    x= np.array([x1, x2])
    w= np.array([-0.5, -0.5])
    b= 0.7
    
    temp = sum(x*w) + b
    
    if temp >= 0:
        return 1
    else:
        return 0


# In[9]:


print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))


# In[10]:


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    
    temp = sum(x*w) + b
    
    if temp>=0:
        return 1
    else:
        return 0


# In[11]:


print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))


# In[12]:


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y= AND(s1, s2)
    
    return y


# In[13]:


print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))


# In[ ]:




