#!/usr/bin/env python
# coding: utf-8

# In[1]:


# daily exercises :  date : 30 nov


# prorame to check leaf year:

# In[2]:


year=int(input("enter year"))
if(year%100==0) and (year%400==0):
    print("{0}is leap year".format(year))
elif(year%4==0) and (year%100!=0):
    print("{0} is leap year".format(year))
else:
    print("{0}is not leap year".format(year))


# check number is positive, nagative , 0:

# In[3]:


number=int(input("enter number"))
if(number>0):
    print("positive")
elif(number<0):
    print("nagative")
else:
    print("0")


# calculate total cost if price is greator 100 aplly discount 10%

# In[4]:


price = int(input("enter price"))
quantity=int(input("enter quantity"))
cost=price*quantity
if(cost>100):
    discount = 0.1  # 10% discount
    discounted_amount = cost * discount
    cost -= discounted_amount
    print(f"Total cost after a 10% discount: ${cost:.2f}")
else:
    print(cost)


# check number is even or odd

# In[5]:


number=int(input("enter number"))
if(number%2==0):
    print("even")
elif(number%2!=0):
    print("odd")
else:
    print("invalid number")


# build grade programed

# In[6]:


grads=float(input("enter grade: "))
if(grads>=90):
    print("A:excellent")
elif(grads>=80 and grads<=89):
    print("B:good")
elif(grads>=70 and grads<=79):
    print("c: satisfactory")
else:
    print("F: needs improvment")


# 
