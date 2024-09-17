#!/usr/bin/env python
# coding: utf-8

# # TASK 2 
# ### Calculate Summary Statistics

# ## Calculate Mean, Median, and Standard Deviation

# In[17]:


import numpy as np
import pandas as pd
train_data = pd.read_csv('train.csv')
# Selecting only Numerical Columns and then find Mean, Median and Standard Deviation
numerical_cols = train_data.select_dtypes(include=['int64', 'float64'])
mean_values = numerical_cols.mean()
median_values = numerical_cols.median()
std_values = numerical_cols.std()
print("Mean Values:")
print(mean_values)
print("\nMedian Values:")
print(median_values)
print("\nStandard Deviation Values:")
print(std_values)


# ##  Calculate Summary Statistics for Numerical Columns

# In[18]:


numerical_cols = train_data.select_dtypes(include=['int64', 'float64'])
summary_stats = numerical_cols.describe()
print("Summary Statistics:")
print(summary_stats)


# ## Calculate Correlation Matrix
# 

# In[19]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
train_df = pd.read_csv('train.csv')
numerical_cols = train_data.select_dtypes(include=['int64', 'float64'])
corr_matrix = numerical_cols.corr()
print("Correlation Matrix:")
print(corr_matrix)
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title("Correlation Matrix")
plt.show()


# In[ ]:




