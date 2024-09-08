#!/usr/bin/env python
# coding: utf-8

# ## We use Train.csv Dataset for this Internship

# In[64]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[65]:


# loading the dataset using read_csv available in pandas
data = pd.read_csv("train.csv")
data


# In[66]:


#head- shows the first five entries in the data
data.head()


# In[67]:


# we gather Information about the data
data.info()


# In[68]:


# getting sum of null values in the data 
data.isnull().sum()


# ## TASK 1:   PERFORMING DATA CLEANING 
# ### > Clean a dataset by removing missing values and outliers
# 

# # cleaning the Dataset using fillna 
# 

# In[69]:


# we replace the age null with mean or median of passengers
data['Age'].fillna(data['Age'].median())


# In[70]:


# for cabins name that are empty simply you can drop them or fill with unkown value
data['Cabin'].fillna('Unknown')


# In[71]:


# for Embarked Attribute We use Most Frequently repeated value using mode() function
data['Embarked'].fillna(data['Embarked'].mode()[0])


# In[44]:


# verification if all the missing values are removed or not !
data.isnull().sum()


# ## Handling Outliers

# In[72]:


# Imagine data as a line of numbers. Outliers are numbers that don't fit with the rest. To clean them:
# For this we keep middle aged people (from 25 - 50 years) and remove old aged and children
# Similar to age we keep middle fares and remove very cheap and high Fares


# In[73]:


# We use function for removing the outliers
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q2 = df[column].quantile(0.75)
    IQR = Q2 - Q1
    low_bnd = Q1 - 1.5 * IQR
    up_bnd = Q2 + 1.5 * IQR
    return df[(df[column] >= low_bnd) & (df[column] <= up_bnd)]
data = remove_outliers(data, 'Age')
data = remove_outliers(data, 'Fare')
data.to_csv('clean.csv', index = False)


# In[74]:


import seaborn as sns
clean = pd.read_csv('clean.csv')
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(y=data['Age'])
plt.title('Age - Before Removing Outliers')
plt.subplot(2, 2, 2)
sns.boxplot(y=data['Fare'])
plt.title('Fare - Before Removing Outliers')
plt.subplot(2, 2, 3)
sns.boxplot(y=clean['Age'])
plt.title('Age - After Removing Outliers')
plt.subplot(2, 2, 4)
sns.boxplot(y=clean['Fare'])
plt.title('Fare - After Removing Outliers')
plt.tight_layout()
plt.show()


# In[75]:


clean = pd.read_csv('clean.csv')
print("\nSummary before Removing Outliers")
print(data[['Age', 'Fare']].describe())
print("\nSummary After Removing Outliers")
print(clean[['Age', 'Fare']].describe())


# In[ ]:




