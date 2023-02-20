# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:06:57 2022

@author: 20050
"""


import numpy as np

X=np.array([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,
            39.42,26.71,35.00])
name=np.array(['Allied Signal','Allied Signal','General Mills','ITT Industries',
               'J.P.Morgan & Co.','Lehman Brothers','Marriott','MCI','Merrill Lynch',
               'Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways',
               'Warner-Lambert'])

import pandas as pd
pd.DataFrame(X)
pd.DataFrame(name)


##Pie plot

import matplotlib.pyplot as plt
plt.figure(figsize=(7,9))
plt.pie(X,labels=name,autopct='%2.0f%%')
plt.show()

### Boxplot

import seaborn as sns
sns.boxplot(X,color='blue')

## find out  μ,σ,σ^2

X.mean() ## Mean
X.std()  ## Standard Deviation
X.var()  ## Variance


###

# If 1 in 200 long-distance telephone calls are getting misdirected.

n=5 ## number of calls 
p=0.005 # probalility of call misdirecting= 1/200
q=0.995 ## probalility of call not misdirecting = 1-1/200 = 199/200

P(x)= at least one in five attempted telephone calls the wrong number

from scipy.stats import binom
bi= binom(5,0.005) ## n,p
1-bi.cdf(0).round(3)

# 2% chance at least one in five attempted telephone calls reaches the wrong number 














































































