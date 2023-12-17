#!/usr/bin/env python
# coding: utf-8

# # sets and tupls methods

# sets methods

# In[15]:


set1={1,2,3,5,5,6,7,8,90}
set2={122,3,65,5,7,7,8,99}


# In[2]:


set1.add(12,11)


# In[3]:


set1.add(112)


# In[4]:


set1


# In[5]:


set1.remove(112)


# In[6]:


set1


# In[7]:


set1.update(122,654)


# In[8]:


set1.update([124,56,67])


# In[9]:


set1


# In[10]:


set1.discard(5)


# In[11]:


set1


# In[12]:


set1.pop()


# In[13]:


set1.pop(4)


# In[16]:


set1.union(set2)


# In[17]:


set1.intersection(set2)


# In[18]:


set1.difference(set2)


# In[19]:


set2.symmetric_difference(set1)


# In[21]:


set1.issubset(set2)


# In[23]:


set1.issubset(set2)


# In[24]:


set1.isdisjoint(set2)


# In[25]:


set3=set1.copy()


# In[26]:


set3


# In[27]:


len(set3)


# In[28]:


9 in set3


# In[29]:


9 not in set3


# In[30]:


set3 = {x for x in range(10) if x % 2 == 0}
print(set3)


# In[31]:


set2[2:3]


# In[32]:


set3.clear()


# In[33]:


set3


# # tupls methods

# In[35]:


t1=(1,2,3,45,6,7,8,2,3,4,45,5,54,3,12,3,34,55,6,6,55,6,6,)


# In[36]:


t1.append(23)


# In[37]:


t1.index(4)


# In[40]:


t1.count()


# In[41]:


t1.count(6)


# In[42]:


t1[2]=323


# In[43]:


5 in t1


# In[44]:


5 not in t1


# In[45]:


t1.sorted()


# In[46]:


sorted(t1)


# In[47]:


reverse(t1)


# In[48]:


sorted(t1,reverse=True)


# In[49]:


t1


# In[ ]:




