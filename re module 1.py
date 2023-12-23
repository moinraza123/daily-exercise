#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
pattern = r"apple"
text =  r" i like apple and orange"
match = re.search(pattern,text)
if match:
    print("found : ",match.group())


# In[3]:


import re

pattern = r"apple"
text = "I like apples and oranges."

match = re.match(pattern, text)
if match:
    print("Found at the beginning:", match.group())


# In[4]:


import re 
pattern = r"apple"
text = r"i like apple and applesausec"
matches = re.findall(pattern, text)
print("all matches : ",matches)


# In[5]:


import re
pattern  = r"apple"
replacement = "orange"
text = "i like apple and applesausec"
new_text = re.sub(pattern, replacement, text)
print("new text : ",new_text)


# In[6]:


import re
pattern = r"app\w+"
text = "i like apples and applesausec"
matches = re.finditer(pattern, text)
for match in matches:
    print("find : ",match.group())


# In[7]:


import re
pattern = r"\s+"
text = "i like apples and applesauces"
word = re.split(pattern, text)
print("words: ",word)


# In[ ]:




