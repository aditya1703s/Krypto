#!/usr/bin/env python
# coding: utf-8

# In[91]:


from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


# In[93]:


import pandas as pd
import time
import smtplib
import requests


# In[94]:


t = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", headers = {"accept": "application/json"})
dict = t.json()
value = dict['bitcoin']['usd']
value


# In[ ]:


sender_email = input("Enter sender's mail address : ")


# In[ ]:


password = input("Enter sender's mail password : ")


# In[ ]:


rec_email = input("Enter receiver's mail address : ")


# In[ ]:


target_sell_price = int(input("Enter target sell price : "))


# In[ ]:


choice = input("Enter 1 if you want to be bullish Enter 2 if bearish")


# In[ ]:


if choice == 1:
    bullish()
elif choice == 2:
    bearish()
def bullish():
    message = "Bitcoin Price Alert" + "%.6f" % value 
    if value >= target_sell_price:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login Success")
        server.sendmail(sender_email, rec_email, message)
        print("Email was sent")
def bearish():
    message = "Bitcoin Price Alert" + "%.6f" % value 
    if value <= target_sell_price:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login Success")
        server.sendmail(sender_email, rec_email, message)
        print("Email was sent")


# In[ ]:





# In[ ]:




