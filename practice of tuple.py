#!/usr/bin/env python
# coding: utf-8

# In[1]:


# paractice of tupls


# In[3]:


fruits=('mango','banana','orange')


# In[4]:


fruits[1]


# In[5]:


#1 Slice a tuple:


# In[8]:


subset=fruits[:2]


# In[9]:


subset


# In[10]:


#2 Concatenate tuples:


# In[14]:


more_fruits=('graphs','kiwi')


# In[15]:


all_fruits=more_fruits+fruits


# In[16]:


all_fruits


# In[17]:


more_fruits


# In[18]:


#3 Check if an element exists in a tuple:


# In[20]:


fruit_name=input("entere name of fruits : ")


# In[23]:


if fruit_name in all_fruits:
    print("available in store")
else:
    print("out of stock")


# In[24]:


#4 Find the index of an element:


# In[25]:


banana_index=all_fruits.index('banana')


# In[26]:


banana_index


# In[27]:


#5 Count occurrences:


# In[32]:


count_banana=all_fruits.count('banana')


# In[33]:


count_banana


# In[ ]:




