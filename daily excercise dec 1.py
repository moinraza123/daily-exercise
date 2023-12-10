#!/usr/bin/env python
# coding: utf-8

# In[1]:


#daily excercise date 1 dec


# In[3]:


string=input("enter string: ")
if(len(string)>=10):
    print("string is long")
else:
    print("string is short")


# check number is divisible by 3 and 5:

# In[5]:


number=int(input("enter number: "))
if(number%3==0 and number%5==0):
    print("disible by 3,5")
elif(number%3==0 and number%5!=0):
    print("divisible by 3 not 5")
elif(number%5==0 and number%3!=0):
    print("divisible by 5 not 3")
else:
    print("not divisible by both")


# check vote eligibility of person

# In[6]:


age=int(input("enter age"))
if(age>=18):
    print("eligible")
else:
    print("nt eligible")


# In[7]:


miles=int(input("enter miles: "))
if(miles>3):
    extra=miles-3
    cost=extra*1
    print("total extra cost: ",cost)
else:
    print("no additional cost")


# give student to grads

# In[8]:


grads=float(input("enter marks"))
if 0 <= grads <= 100:
    if(90<=grads<=100):
        print("A")
    elif(80<=grads<=89):
        print("B")
    elif(70<=grads<=79):
        print("C")
    elif(60<=grads<=69):
        print("D")
    else:
        print("F")
else:
    print("invalind input")


# In[ ]:




