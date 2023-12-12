#!/usr/bin/env python
# coding: utf-8

# In[5]:


class bank:
    def __init__(self):
        self.balance = 100000
        self.name = " shaikh moin"
        self.account= "12xxxxxxxxxxx56"
        self.total_amount=0
        self.trans_amount=0
        self.withd_amount=0
        self.trans_amoun=0
    def info(self):
        print("balance",self.balance)
        print("name",self.name)
        print("account",self.account)
    def deposit(self):
        self.balance += int(input("enter amount"))
        self.total_amount += self.balance
        print("total amount : ",self.total_amount)
    def withdraw(self):
        self.withd_amount = int(input("enter amount"))
        self.balance -= self.withd_amount
        print("withdraw amount : ",self.withd_amount)
        print("total amount : ",self.balance)
    def  transfer(self):
        self.trans_amount = int(input("enter amount"))
        self.balance -= self.withd_amount
        print("withdraw amount : ",self.trans_amount)
        print("total amount : ",self.balance)


# In[6]:


pin=int(input("enter pin"))
if (pin==9043):
    while(1):
        p1=bank()
        ch=int(input("entre your choice \n1.info\n2.deposite\n.3withdraw\n4.transfer\n.5exit"))
        if(ch==1):
            p1.info()
        elif(ch==2):
            p1.deposit()
            p1.info()
        elif(ch==3):
            p1.withdraw()
            p1.info
        elif(ch==4):
            p1.transfer()
            p1.info
        else:
            break
else:
    print("invalid pin")


# In[ ]:




