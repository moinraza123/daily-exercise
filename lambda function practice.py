#!/usr/bin/env python
# coding: utf-8

# In[3]:


square= lambda x : x**2
x = float(input("enter number"))
print(f"squre is : {x}")


# In[18]:


user_input = input("enter numbers")
str_numbers = user_input.split()
numbers = [int(num) for num in str_numbers]
even_number = map(lambda x : x**2, numbers)
print("enven numbers : ",list(even_number))


# In[20]:


user_input = input("enter number include sapce : ")
str_num = user_input.split()
numbers = [int(num) for num in str_num]
even_num = filter(lambda x : x%2==0,numbers)
print(f"all even numbers : {list(even_num)}")


# In[41]:


user_input = input("enter strng by sepreted spaces")
words = user_input.split()
sorted_words = sorted(words, key=lambda x : len(x))
print("sorted list of string : ",sorted_words)


# In[43]:


add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"

result_add = add(5, 3)
result_subtract = subtract(8, 4)
result_multiply = multiply(2, 6)
result_divide = divide(10, 2)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)


# In[47]:


from  functools import reduce
user_input = input("enter numbers include spaces")
str_num = user_input.split()
numbers = [int(num) for num in str_num]
product = lambda x,y:x*y
result = reduce(product, numbers)
print("product of the numbers : ",result)


# In[48]:


numbers = [ 12,8,25,10,2]
threshold = 20
isgreator_threshold= lambda x: x>threshold
result = any(map(isgreator_threshold, numbers))
print(f"atleast have a greator value {threshold} than = {result}")


# In[ ]:




