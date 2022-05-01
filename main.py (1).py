#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[21]:


import streamlit as st

import sys

import pandas as pd

import altair as alt




# In[22]:


header = st.container()

dataset = st.container()

features =st.container()

modeltraining = st.container()


# In[23]:


with header:
    st.title("Data visulization Project")
    


# In[24]:


with dataset:
    st.header("Data visulization Project")
    
    sales_data = pd.read_csv(r'https://gist.githubusercontent.com/Kiran3295/5b8b4ef58453253473f31efd2a3b9ad2/raw/d3b6b486e7da4640547911e09cfee26f3674d7bd/Sales_Dataset.csv')
    st.write(sales_data.head())
    
    st.subheader('Sales Data')
    a = pd.DataFrame(sales_data['Sales'].value_counts()).head(50)
    st.bar_chart(a)


# In[25]:


with features :
    st.header("Data visulization Project")
    
    sales_data = pd.read_csv(r'C:\Users\91738\OneDrive\Desktop\DV_Project\data\Sales_Dataset.csv')
    
    chart = (alt.Chart(sales_data)# including the csv file
    .encode(
       x='Sales Agent ID', # adding the X value
       y='Sales',# adding the Y value
       color = "State",# adding the color value
       tooltip=['Sales Agent ID', 'Sales', 'State']
       ).mark_circle()# Making it as circular representation
       ).interactive()
    chart.display()# displaying the data


# In[26]:


with modeltraining :
    st.header("Data visulization Project")


# In[27]:





# In[ ]:




