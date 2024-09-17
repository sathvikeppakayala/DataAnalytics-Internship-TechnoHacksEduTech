#!/usr/bin/env python
# coding: utf-8

# # TechnoHacks EduTech Internship TASK 3
# ## Visualization using Histogram

# ### We use Iris Data Set for this Task

# In[57]:


# importing all the Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[58]:


# Loading the Dataset Iris using seaborn
data = sns.load_dataset("iris")
print(data)


# In[59]:


# getting Datatypes of the columns names using dtyes - in python
data.dtypes


# In[60]:


# getting Summary of the Columns names using describe() - in python
data.describe()


# In[61]:


# getting Summary using info() - in python
data.info()


# ## Visualization using Histogram using Matplotlib.pyplot

# In[62]:


# histogram for sepal Length
plt.hist(data['sepal_length'], bins  = 10, alpha = 1, edgecolor = 'k', color = "red")
plt.grid(alpha = 0.5, color = 'black', linestyle = "-.")
plt.title("Histogram For Sepal Lentgh in cm")
plt.xlabel("Sepal Length (in cm)")
plt.ylabel("Frequency")
plt.show()


# In[63]:


# Represting Histogram for sepal width
plt.hist(data['sepal_width'], bins = 10, edgecolor= 'black', alpha = 1, color = "green")
plt.xlabel('Sepal Width (in Cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Width')
plt.grid(color = "black", alpha = 0.5, linestyle = "--")
plt.show()


# In[64]:


# Histogram for petal width 
plt.hist(data['petal_width'], bins = 10, edgecolor = 'black', alpha = 1, color = "orange")
plt.xlabel('Petal Width (in Cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Width')
plt.grid(color = "black", alpha = 0.5, linestyle = "-.")
plt.show()


# In[65]:


# Histogram for petal Length
plt.hist(data['petal_length'], bins = 10, edgecolor = 'black', alpha = 1, color = "pink")
plt.xlabel('Petal Length Cm')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length')
plt.grid(color = "black", alpha = 0.5, linestyle = ":")
plt.show()
     


# In[66]:


# Distribution of Species
species_count = data['species'].value_counts()
plt.bar(species_count.index, species_count.values, edgecolor = "black", alpha = 1, color = "cyan")
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.title('Distribution of Species')
plt.grid(color = "black", alpha = 0.5, linestyle = "-.")
plt.show()


# In[ ]:




