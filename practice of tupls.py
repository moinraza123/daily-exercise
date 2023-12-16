#!/usr/bin/env python
# coding: utf-8

# In[1]:


#practice of set 


# In[2]:


A = {1, 2, 3, 4, 5}


# In[3]:


B = {4, 5, 6, 7, 8}


# In[4]:


#1 Find the union of sets A and B.


# In[5]:


result = A.union(B)


# In[6]:


result


# In[7]:


#2 Find the intersection of sets A and B.


# In[8]:


intersection_result = A.intersection(B)


# In[9]:


intersection_result


# In[10]:


A={1, 2, 3, 4, 5}


# In[14]:


B = {4, 5, 6, 7, 8}


# In[15]:


intersection_result = A.intersection(B)


# In[16]:


intersection_result


# In[17]:


#3 Find the difference between sets A and B.


# In[18]:


diff = A.difference(B)


# In[19]:


diff


# In[20]:


#4 Find the symmetric difference between sets A and B.


# In[21]:


symetric_diff= A.symmetric_difference(B)


# In[22]:


symetric_diff


# In[23]:


#5 Check if set A is a superset of set B.


# In[24]:


subset  = A.issubset(B)


# In[25]:


subset


# In[ ]:




