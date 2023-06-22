#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np

x = np.array([-1.0, 1.0, 2.0])

print(x)
print(x.dtype)


# In[4]:


y = x>0
print(y) # in Numpy, element-wise boolean operation


# In[6]:


y = y.astype(int) # can use np.int instead
print(y)


# ## Step function

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

def step_function(x): # return type : numpy array
    return np.array(x>0, dtype=int)


# In[19]:


x = np.arange(-5, 5, 0.01)
y = step_function(x)

plt.plot(x, y, 'g')
plt.title('step function')
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-2,2)
plt.plot(x, np.zeros(1000,), 'r--')


# ## Sigmoid

# In[21]:


def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return np.array(y)


# In[23]:


x = np.arange(-5,5,0.001) #np.arange : make array with min -5, max 5, interval 0.001
y = sigmoid(x)

plt.plot(x,y, 'b')
plt.plot(x, np.zeros(10000,), 'r--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Sigmoid")
plt.ylim(-1.5, 1.5)

plt.show()


# In[26]:


x = np.arange(-5,5,0.001)
y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x,y1, 'b', x, y2, 'r')
plt.plot(x, np.zeros(10000,), 'g--')
plt.ylim(-0.1, 1.5)
plt.title("Step vs Sigmoid")
plt.xlabel("x")
plt.ylabel("y")


plt.show()


# ## ReLU

# In[27]:


def ReLU(x):
    return np.maximum(0, x)


# In[30]:


x= np.arange(-5,5, 0.01)
y= ReLU(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("ReLU")
plt.legend("ReLU")

plt.show


# In[ ]:




