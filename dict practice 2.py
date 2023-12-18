#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dictionary


# In[6]:


student = {"name" : "shaikh moin","age" : 20, "grade" : "A"}


# In[7]:


name = student["name"]


# In[8]:


name


# In[9]:


age = student["age"]


# In[10]:


age


# In[11]:


#2 Updating Values


# In[12]:


student["age"] = 22


# In[15]:


student


# In[16]:


student["name"] = "annas"


# In[17]:


student


# In[18]:


#3 Adding a New Key-Value Pair


# In[19]:


student["course"] = "data science"


# In[20]:


student


# In[21]:


#4 Iterating Over Keys and Values


# In[22]:


for key,value in student.items():
        print(f"{key} : {value}")


# In[23]:


#5 Removing a Key-Value Pair


# In[24]:


del student["course"]


# In[25]:


student


# In[26]:


#Check if Key Exists


# In[27]:


if "grade" in student:
    print("grade is exist")
else:
    print("grade is not exist")


# In[28]:


#Dictionary Comprehension


# In[29]:


squared_numbers = {num: num**2 for num in range(1, 20)}
print(squared_numbers)


# In[30]:


#9: Merging Dictionaries


# In[31]:


dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}


# In[32]:


merge_dict = {**dict1,**dict2}


# In[33]:


merge_dict


# In[34]:


#10: Dictionary Methods


# In[35]:


key_list= list(student.keys())


# In[36]:


key_list


# In[37]:


value_list = list(student. values())


# In[38]:


value_list


# In[39]:


item_list = list(student.items())


# In[40]:


item_list


# In[ ]:




