Titanic Dataset Cleaning and Analysis
Overview
This repository contains a Python project that performs data cleaning and analysis on the Titanic dataset. The dataset is cleaned by removing missing values and outliers, and then analyzed using various statistical and visualization techniques.

Dataset
The dataset used in this project is the Titanic dataset, which contains information about passengers on the Titanic, including their demographics, ticket information, and survival status.

Files
train.csv: The original Titanic dataset.
clean.csv: The cleaned dataset after removing missing values and outliers.
README.md: This file.
script.py: The Python script that performs data cleaning and analysis.
Data Cleaning
The data cleaning process involves the following steps:

Removing missing values: Missing values in the Age, Cabin, and Embarked columns are replaced with median, 'Unknown', and most frequent value, respectively.
Removing outliers: Outliers in the Age and Fare columns are removed using the Interquartile Range (IQR) method.
Analysis
The cleaned dataset is then analyzed using various statistical and visualization techniques, including:

Summary statistics: Mean, standard deviation, minimum, maximum, and quartiles are calculated for the Age and Fare columns.
Box plots: Box plots are created to visualize the distribution of Age and Fare before and after removing outliers.
Requirements
Python 3.x
Pandas library
NumPy library
Matplotlib library
Seaborn library
