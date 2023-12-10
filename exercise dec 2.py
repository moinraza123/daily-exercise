#!/usr/bin/env python
# coding: utf-8

# In[1]:


#date : Dec 2


# while loop exercise

# In[2]:


count = 0
while count < 5:
    print(count)
    count += 1


# In[3]:


# use the else with a while loop


# In[4]:


count =int(input("enter number: "))
while(count<5):
    print(count)
    count += 1
else:
    print("loop is ended")


# The pass statement in Python is a no-operation statement

# In[5]:


count = 0
while(count<5):
    print(count)
    count += 1
    pass
print("loop is ended")


# The sum of the first 10 even numbers

# In[6]:


sum1 = 0
count = 1
while(count<=10):
    sum1+= count * 2
    count += 1
print(sum1)


# guess the number

# In[7]:


import random

secret_number = random.randint(1, 10)
user_guess = 0
while user_guess != secret_number:
    user_guess = int(input("Guess the number (between 1 and 10): "))
    if user_guess < secret_number:
        print("Too low. Try again.")
    elif user_guess > secret_number:
        print("Too high. Try again.")
print("Congratulations! You guessed the number.")


# In[ ]:




