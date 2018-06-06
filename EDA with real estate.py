# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:24:27 2018

@author: vuppuluri
"""

import pandas as pd
from sklearn import tree
from sklearn import model_selection
import os

os.chdir("D:")
a = pd.read_csv("D:\\Real_estate_data.csv")

print(os.getcwd())   ##Get the current working directory


year=[1930,1940,1950,1960,1970]   # Sample data for x-axis
growth=[30,40,70,100,200]    #Sample data for Y-axis
color=['red','green','yellow','blue','orange'] ##color of the bubble in scatter plot
size=np.array(growth)  ### Size of the bubble in scatter plot
plt.xlabel('years')
plt.ylabel('Growth')
plt.title('GRAPH')
plt.text(140, 71, 'India')  # middle of the graph dispalys india 
plt.text(160, 130, 'China') # middle of the graph dispalys india

### Know more about xticks and yticks


plt.plot(year,growth) # Draws linear graph
plt.hist(growth)  # Draws histogram default bins=10
plt.hist(growth,2)  # Draws histogram default bins=2
plt.scatter(year,growth,s=size,c=color)    ##Draws scatter graph year and growth are mandarory .size and color are optional
# There is a alpha value in scatter plot ..check on that

plt.show()
