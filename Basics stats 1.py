"""
Created on Sun Nov 13 12:01:50 2022

@author: 20050
"""

####Import the data

import pandas as pd
df=pd.read_csv("C:\\Data Science\\Assignments\\Basic Statistics\CSV files\\Q7.csv")
df

##for points(Mean,median,std,variance,mode,range)

df[["Points"]].mean()### Mean
df[["Points"]].median()##Median
df[["Points"]].mode()#mode
df[["Points"]].std()#standard Deviation
df[["Points"]].var()#Variance
df[["Points"]].max()-df[["Points"]].min()##Range

##for Score(Mean,median,std,variance,mode,range)

df[["Score"]].mean()### Mean
df[["Score"]].median()##Median
df[["Score"]].mode()#mode
df[["Score"]].std()#standard Deviation
df[["Score"]].var()#Variance
df[["Score"]].max()-df[["Score"]].min()##Range

##for Weigh(Mean,median,std,variance,mode,range)

df[["Weigh"]].mean()### Mean
df[["Weigh"]].median()##Median
df[["Weigh"]].mode()#mode
df[["Weigh"]].std()#standard Deviation
df[["Weigh"]].var()#Variance
df[["Weigh"]].max()-df[["Score"]].min()##Range


###  

import pandas as pd
df=pd.read_csv("C:\\Data Science\\Assignments\\Basic Statistics\\Q9_a.csv")
df


##For speed(Skewness and Kurtosis)

df[["speed"]].skew()## Skewness
df[["speed"]].kurt()## Kurtosis

##Conclusion:
#Negative values for the skewness indicates that data is skewed towards left &
#Positive values for the skewness indicates that data is skewed towards right.
#If skewed is towards left,we can say that left tail is long realtive than right.
#Distribution has a negative Kurtosis,it is said to be platykurtic, which means,
#that it has flatter peaks and thinner tails compared to normal distribution


##For dist(Skewness and Kurtosis)

df[["dist"]].skew()## Skewness
df[["dist"]].kurt()## Kurtosis

#Conclusion

#In a positive skewness, the tail of the distribution curve is longer on the,
#right side. This means that the outliers of the distribution curve are further,
##out towards right and closer to the mean on the left.
#Positive value of the kurtosis indicates that distribution is peaked and ,
#possesses thick tail and it is known as Leptokurtic.



###
import pandas as pd
df=pd.read_csv("C:\\Data Science\\Assignments\\CSV files\\Q9_b.csv")
df

##For SP(Skewness and Kurtosis)

df[["SP"]].skew()
df[["SP"]].kurt()

#Conclusion

#In a positive skew, the tail of distribution curve is longer on the right side,
#This means that the outliers of the distribution curve are further,out towards
#right and closer to the mean on the left.
#Positive value of the kurtosis indicates that distribution is peaked and ,
#possesses thick tail and it is known as Leptokurtic.


##For WT(Skewness and Kurtosis)

df[["WT"]].skew()
df[["WT"]].kurt()

#Conclusion

#Negative values for the skewness indicates that data is skewed towards left &
#Positive values for the skewness indicates that data is skewed towards right.
#If skewed is towards left,we can say that left tail is long realtive than right.
#Positive value of the kurtosis indicates that distribution is peaked and ,
#possesses thick tail and it is known as Leptokurtic.



##

mean=200
SD=30
n=2000

from scipy import stats

from scipy.stats import norm


##Avg weight of adult in Mexico with 94% CI

stats.norm.interval(0.94,200,30/(2000**0.5))


##Avg weight of adult in Mexico with 94% CI

stats.norm.interval(0.96,200,30/(2000**0.5))


##Avg weight of adult in Mexico with 94% CI

stats.norm.interval(0.98,200,30/(2000**0.5))



####
 
import numpy as np

test=np.array([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
test

#Calculate mean,median,varaince,standard deviation

np.mean(test)
np.median(test)
np.std(test)
np.var(test)



################# 

import pandas as pd

df=pd.read_csv("C:\\Data Science\\Assignment\\CSV files\\Cars.csv")
df
df.dtypes

import numpy as np
np.mean(df).round(3)
np.std(df).round(3)

from scipy.stats import norm
nd=norm(34.422,9.075)###mean,sd

##P(MPG>38)
1-nd.cdf(38).round(3)

#P(MPG<40)
nd.cdf(40).round(3)

#P(20<MPG<50)
x2=nd.cdf(50).round(3) ## 0 to 50
x2
x1=nd.cdf(20).round(3) ##0 to 20
x1

x2-x1





###### 
import scipy.stats as stats

##Z value for 98% confidence interval
stats.norm.ppf(0.05).round(3)

##Z value for 94% confidence interval
stats.norm.ppf(0.03).round(3)


##Z value for 60% confidence interval
stats.norm.ppf(0.2).round(3)



############

df=25
df

##T score for 99% confidence interval

stats.t.ppf(0.025,25).round(3)

##T score for 95% confidence interval

stats.t.ppf(0.005,25).round(3)


##T score for 96% confidence interval

stats.t.ppf(0.006,25).round(3)




####


mean=260
sd=90
n=18

from scipy.stats import stats

#Assume Null hypothesis is:H0=Avg life of bulb = 260 days
#Alternative hypothesis is H1= Avg life of bulb = 260 days
#find t-score at x=260, t=(s_mean-P_mean)/(s_SD/sqrt(n))

t=(260-270)/(90/18**0.5)
t

from scipy.stats import norm
## find p(X>=260) for null hypothesis

# P_value=1-stats.t.cds(abs(t_scores),df=n-1)
p_value=1-stats.p.cdf(abs(-0.4714),df-17)
p_value
















































