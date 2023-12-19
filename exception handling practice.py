#!/usr/bin/env python
# coding: utf-8

# # exception handling practice

# In[1]:


def perform_division():
    try:
        num1 = float(input("enter numratore"))
        num2 = float(input("enter dominator"))
        result = num1 / num2
    except ValueError:
        print("Error : invalid input.  enter numric value")
    except ZeroDivisionError:
        print("error : cannot divide by Zero")
    else:
        print(f"the result of {num1} divide by {num2} is : {result}")
    finally:
        print("execution is complete")


# In[2]:


perform_division()


# In[3]:


try:
    num_list = input("enter a list of numbers (sepreted by coma) : ").split(',')
    for num_str in num_list:
        try:
            num = float(num_str)
            if num %2 == 0:
                square_result = num**2
                print("\n"f"the square of {num} is : {square_result}")
            else:
                division_result= 10 / num
                print("\n"f"the {num} division by 10 result is : {division_result}")
        except ValueError:
            print(f"error : {num_str} is not valid numeric value")
        except ZeroDivisionError:
            print(f"{num} cannot divid by zero")
        except exception as e:
            print(f"error : an unexcepted error occurd-{e}")
except KeyboardInterrupt:
    print("\n programe terminated by usre")
else:
    print("\n programe complete succesfully")
finally:
    print("\n programe excution complete")


# In[4]:


try:
    strings = ["level","12321","hello","radar","world"]
    for s in strings:
        try:
            is_palindrome = s == s [::-1]
            if is_palindrome:
                print(f"\n string {s} is palindrome")
            else:
                try:
                    convert_int = int(s)
                    print("\n"f"the string {s} is not palindrome but convert to an integer : {convert_int}")
                except ValueError:
                    print("\n"f"error : the string {s} is neigther palindrome or a valid integer")
        except Exception as e:
            print(f"\n error : an unexpted error occurd-{e}")
except KeyboardInterrupt:
    print("\n programe terminated by the user")
else:
    print("\n programe complete succsfull")
finally:
    print("\n progarme excution complete")


# In[5]:


import math
def procces_numbers(numbers):
    for num in numbers:
        try:
            if num > 0 :
                try:
                    sqrt_result = math.sqrt(num)
                    if sqrt_result == int(sqrt_result):
                        print(f"\n the number {num} has integer sqrt is : {int(sqrt_result)}")
                    else:
                        print(f"\n the number {num} non integer sqrt is : {sqrt_result}")
                except ValueError:
                    print(f"\n error : unbale to calculate the sqrt of {num}")
                except Exception as e:
                    print(f"\n error occurd : {e}")
            else:
                print(f"\n number '{num}' is not positive")
        except Exception as e:
            print("\n error {e}")
try:
    number_values = [16,-5,25,8,10,"moin"]
    procces_numbers(number_values)
except KeyboardIntrrupt:
    print("\n programme terminated by user ")
else:
    print("\n programe completed succesfully")
finally:
    print("\n programe excution complete")


# In[ ]:




