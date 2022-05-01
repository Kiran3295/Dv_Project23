#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

import pandas as pd 
import altair as alt

import sys


# In[8]:


url = "https://gist.githubusercontent.com/Tulluripallavi/983092b3b60760198dc778117141ac55/raw/bbba5e8e8f1c94e297c492cd33975aa97da1f056/salesdisaster.csv"
mpg = pd.read_csv(url)


# In[9]:


header = st.container()

dataset = st.container()

features =st.container()

modeltraining = st.container()


# In[10]:


with header:
    st.title("Data visulization Project")


# In[11]:


with dataset:
    chart = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Quantity',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Quantity', 'State']
    )
  .mark_boxplot()# Making it as boxplot representation
).interactive()
chart.encode(x='Sales Agent ID')


# In[ ]:




