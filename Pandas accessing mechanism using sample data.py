# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:45:58 2018

@author: vuppuluri
"""

import pandas as pd
from sklearn import tree
from sklearn import model_selection
import os

os.chdir("D:")
pd_sample = pd.read_csv("D:\\Real_estate_data.csv",index_col=0) ## Assign the first column as row identifier,
pd_sample = pd.read_csv("D:\\Real_estate_data.csv",index_col=1) ## Reads data the as it is  and assign virtual row index as 0 1 2 

print(os.getcwd())

print(pd_sample.head(5)) ##Prints first records as data frame
print(pd_sample.tail(5)) ##Prints last records as data frame
print(pd_sample[[1]]) ## Throws error as positional index can be used without iloc
print(pd_sample["Status"])  ## Displacy Status columns alone as pandas.core.series.Series 
print(type(pd_sample[["Status"]])) ## Displacy Status columns alone as pandas.core.frame.DataFrame

##Advanced methods to access pands are ising loc(lable based) and iloc (position based)

print(pd_sample.loc[:,['Status','Price']])  ## displays all the recrods status and price as data frame
print(pd_sample.loc[[1],['Status','Price']])  ## Fails as postional index not allowed in loc

pd_sample = pd.read_csv("D:\\Real_estate_data.csv",index_col=0)
print(pd_sample.loc[['Granite Northland Associates'],['Status','Price']]) ## Records can be read as row identifier if the file is read as index_Col=0
print(pd_sample.loc[:,['Status','Price']])  ## displays all the recrods status and price as data frame
print(pd_sample.iloc[[1],[2]])  ## prints second row third column
print(pd_sample.iloc[1:]) # Prints second row all the columns
print(pd_sample.iloc[:,[2:5]]) # Prints all the records third column
print(pd_sample.iloc[4:,5:9]) # Prints 4th to all rows with 6th columns to 8th 
print(pd_sample.iloc[[3,4],[5,9]]) # Prints 4th and 5th rows and 6th and 10th columns


print(pd_sample)

print (list(pd_sample))

