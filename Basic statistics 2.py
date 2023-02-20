# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:53:41 2022

@author: 20050
"""


mean=38
sd=6

from scipy.stats import norm
nd=norm(38,6) #mean,sd

#probability of employees less than 30 -- P(X=<30)

nd.cdf(30)


# Therefore the statement regarding the training program for employees
# under the age of 30 at the centre would be expected to attract about
# 36 employees is "TRUE"

import numpy as np

#Mean profit for 2 different companies= Mean1 + Mean2
Mean=5+7

print("Mean profit in Rs",Mean*45,'Million')

# variance of profit for 2 different companies =SD^2=SD1^2+SD2^2

SD=np.sqrt(9)+(16)
print("Standard deviation in Rs",SD*45,'Millions')

from scipy import stats 
from scipy.stats import norm


# A.) Rupee range(Centered on the mean) such that it contains 95% probability
# for the annual profit of the company

print("Range in Rs",(stats.norm.interval(0.95,540,225)),'in Millions')

#B.) The 5th percentile of proifts(in rupees) for the company,to compute 5th 
# percentile, the formula=X-μ + Zσ : wherin from z table,5 percentile= -1.645

X=540+(-1.645)*(225)
print('5th percentile of profit(in Millions Rupees)is',np.round(X,))


#C.) Which of the two division has a larger probability of making a loss in a given year

#probability of Division 1 making a loss=P(X<0)
stats.norm.cdf(0,5,3)

#probability of Division 2 making a loss=P(X<0)
stats.norm.cdf(0,7,4)

#Division have larger chance of making a loss compared to division 2 


import numpy as np

# n= 100, pop mean= 50, pop  SD=40, as no. of samples is more than 30, we can consdier
# it normal distribution

from scipy import stats
#for No investiagtion P(45<X55)
#for Investigation 1-P(45<X<55)

#find z-score at X=45; z=(s_mean-P_mean)/(p_SD/sqrt(n))

Z=(45-50)/(40/100**0.5)
Z

#find z-score at X=55; z=(s_mean-P_mean)/(p_SD/sqrt(n))

Z=(55-50)/(40/100**0.5)
Z

from scipy.stats import norm
#for No inestigation P(45<X<55) using z-score=P(X<50)-P(X<45)
stats.norm.cdf(1.25)-stats.norm.cdf(-1.25)

stats.norm.interval(0.7887,loc=50,scale=40/(100**0.5))

#for investigation 1-P(45<X<55)
1-0.7887



















































