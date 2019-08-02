# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:31:38 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def header(msg):
    print('-'*50)
    print('['+msg+']')

header("1. load hard-coded data into a df")
df=pd.DataFrame(
        [['Jan',58,42,74,22,2.95],
         ['Feb',61,45,78,26,3.02],
         ['Mar',65,48,84,25,2.34],
         ['Apr',67,50,92,28,1.02],
         ['May',71,53,98,35,0.48],
         ['Jun',75,56,107,41,0.11],
         ['Jul',77,57,103,40,0.17],
         ['Aug',77,59,102,43,0.03],
         ['Sep',77,57,103,40,0.17],
         ['Oct',73,54,96,34,0.81],
         ['Nov',64,48,84,30,1.7],
         ['Dec',58,42,73,21,2.56]],
         index = [0,1,2,3,4,5,6,7,8,9,10,11],
         columns=['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

'''
header("2. read text file into a df")
filename = 'weather.txt'
df=pd.read_csv(filename)
print (df)

header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

header("4.df.dtypes")
print(df.dtypes)

header("4.df.index")
print(df.index)

header("4.df.columns")
print(df.columns)

header("4.df.values")
print(df.values)
'''
header("5.df.describe()")
print(df.describe())
'''
header("6.df.sort_values('record_high',ascending=False)")
print(df.sort_values('record_high',ascending=False))


header("7. slicing--df.avg_low")
print(df.avg_low)

header("7.slicing--df['avg_low']")
print(df['avg_low'])

header("7.slicing--df[2:4]")
print(df[2:4])

header("7.slicing--df['avg_low','avg_high']")
print(df[['avg_low','avg_high']])

header("7.slicing scalar value--df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7.df.iloc[3:5,[0,3]]")
print(df.iloc[3:5,[0,3]])

header("8.df[df.avg_precipitaion>1.0]")
print(df[df.avg_precipitation>1.0])

header("9.df.loc[9,['avg_precipitation']]=101.3") #change a data
df.loc[9,['avg_precipitation']]=101.3
print(df.iloc[9:11])

header("9.df.loc[9,['avg_precipitation']]=np.nan") #change a data
df.loc[9,['avg_precipitation']]=np.nan
print(df.iloc[9:11])

header("9.df.loc[:,'avg_low']=np.array([5]*len(df))") #change a column
df.loc[:,'avg_low']=np.array([5]*len(df))
print(df)

header("9.df['avg_day']=(df.avg_low+df.avg_high)/2")#create a new column
df['avg_day']=(df.avg_low+df.avg_high)/2
print(df)

header("10.df.rename(columns={'avg_precipitation':'a'},inplace=True)") #change column name
df.rename(columns={'avg_precipitation':'a'},inplace=True)
print df

header("10.df.columns=['a','b','c','d','e','f']") #change column names
df.columns=['a','b','c','d','e','f']
print(df)


header("11.iterate rows of df with a for loop") #iterate rows
for index,row in df.iterrows():
    print index,row["month"],row["avg_high"]

header("10.df.columns=['a','b','c','d','e','f']") #change column names
df.columns=['a','b','c','d','e','f']
print(df)

header("12.save to csv")
df.to_csv('fo.csv')
'''