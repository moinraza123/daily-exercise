#!/usr/bin/env python
# coding: utf-8

# In[1]:


#practice of list


# In[2]:


list1=['mango','apple','orange','banana','cactus']


# In[3]:


list2=[1,2,3,4,5,6,7,8,9,10]


# In[4]:


#1 List Manipulation:


# In[5]:


list1.append('lemon')


# In[6]:


list1


# In[7]:


#2 List Slicing:


# In[8]:


slic=list2[1:10:2]


# In[9]:


slic


# In[10]:


slic1=list2[10:0:-2]


# In[11]:


slic1


# In[12]:


#3 List Methods:


# In[13]:


list1.append('fruits')


# In[14]:


list1


# In[15]:


list1.insert(3,'moin')


# In[16]:


#4 List Iteration:


# In[17]:


cities = ['jalgaon','pune','nagar','jalna']


# In[18]:


for city in cities:
    print(city)


# In[19]:


#5 Nested Lists:


# In[20]:


matrix=[[1,2,3],[4,5,6],[7,8,9,]]


# In[21]:


matrix


# In[22]:


for row in matrix:
    print(row)


# In[23]:


element=matrix[1][2]


# In[24]:


element


# In[ ]:




