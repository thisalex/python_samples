
# coding: utf-8

# In[1]:

from tabula import read_pdf
import pyhdb
import pandas as pd


# In[8]:

path_to_pdf = r"C:\Users\I335191\dev\python_samples\data\Sample_employees_data.pdf"
df = read_pdf(path_to_pdf ,pages=1,guess=False)


# In[6]:

df


# In[ ]:



