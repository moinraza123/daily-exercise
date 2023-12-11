#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a program to print the * pattern using a for loop:


# In[3]:


#1
for i in range(1,7):
    print('*'*i)


# In[4]:


#2 Write a program to print the * reverse pattern using a for loop:
for i in range(7,0,-1):
    print('*'*i)


# In[5]:


#3 Write a program to print the squares of numbers from 1 to 5 using a for loop.
for i in range(1, 6):
    print(f"The square of {i} is {i**2}")


# In[6]:


#4 takes a string as input from the user and prints each character in the string using a for loop:
user_input = input("Enter a string: ")

print("Each character in the string:")
for char in user_input:
    print(char)


# In[7]:


#5 adition of even and odd:
add=int(input("enter number"))
odd=int(input("enter number"))
for num in range(1,11,):
    if(num%2==0):
         add=add+num
    else:
        odd=odd+num
print(add)
print(odd)


# In[ ]:




