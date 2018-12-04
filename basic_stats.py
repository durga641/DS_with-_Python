# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 06:34:46 2018

@author: Venkat Durga Rao
"""

import os
import pandas as pd
#import dataframes from pandas as df
import numpy as np
import scipy as stats
from sklearn import datasets
import maths as mh
import seaborn as sns


iris_data = datasets.load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = pd.Series(iris_data.target)
iris_df['target1'] = 'Abc'
iris_df.head(6)

list(iris_df.columns)  ## Print the list of columns
len(iris_df.columns) ## count the columns
len(iris_df)  ## count the records
iris_dict=dict(iris_df.dtypes)  ## prints the data type of each column
iris_df['target'].value_counts() #counts the value of each column

print(iris_dict)
#### find the categorical columns
cat_columns=[]
for column in iris_dict:
    if (iris_dict[column]=='int32' or iris_dict[column]=='O' ) :
        cat_columns.append(column)
print(cat_columns)   
############## find the missing values and their percentage  ###

iris_df.isna().sum()
iris_miss=pd.DataFrame()
print(iris_miss)
iris_miss['count']=iris_df.isna().sum()
iris_miss['percent']=iris_miss['count']/len(iris_df)
print(iris_miss)


####################



