#!/usr/bin/env python
# coding: utf-8

# In[1]:


# user define function


# In[2]:


#1 Program to check if a number is prime or not


# In[3]:


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
print(is_prime(5))  
print(is_prime(12))  
print(is_prime(17)) 
print(is_prime(25))


# In[4]:


#2 reverse string
def reverse_string(stri):
    return stri[::-1]
num1=input("enter name")
reverse_string(num1)


# In[5]:


#3count vowels in string


# In[8]:


def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count
num1=input("enter string : ")
print("total vowels",count_vowels(num1))


# In[9]:


#4
def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return common
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_elements(list1, list2)
print(f"Common elements between {list1} and {list2}: {result}")


# In[10]:


#5
def factorial(n):
    if n < 0:
        return None  
    elif n == 0 or n == 1:
        return 1  
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
num=float(input("enter number"))
print(factorial(5))


# In[ ]:




