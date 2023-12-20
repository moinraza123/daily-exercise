#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class person:
    def say_hello(self):
        self.name= input("enter name : ")
        self.age = int(input("enter age : "))
#person1 = person("alice",25)
#print(person1.name)
#print(person1.age)
#greeting = person1.say_hello()
#print(greeting)


# In[26]:


class employee(person):
    def __init__(self):
        self.emp_id= int(input("enter emp id : "))
    def display_info(self):
        print(f"my emp_id : {self.emp_id}.")
        print(f"my name : {self.name}.\nand age is : {self.age}")


# In[27]:


obj = employee()
obj.say_hello()
obj.display_info()


# In[28]:


# atm code 


# In[ ]:


class bank:
    def user_info(self):
        self.accounts = {'shaikh moin',} 

