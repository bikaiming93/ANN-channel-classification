# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:49:38 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def header(msg):
    print('-'*50)
    print('['+msg+']')

filename = 'example1.csv'
df=pd.read_csv(filename)

print(df)
'''
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

header("5.df.describe()")
print(df.describe()) #print df['Score'].describe()

header("6.df.sort_values('Score',ascending=False)")
print(df.sort_values('Score',ascending=False))


header("7.slicing--df['Score']")
print df['Score']

header("7. slicing--df.act_clbk_req_flg")
print(df.act_clbk_req_flg)

header("7.slicing--df[2:4]")
print(df[2:7])

header("7.slicing--df['avg_low','avg_high']")
print(df[['orig_que_typ_cd','orig_que_to_nm']])

header("7.df.iloc[3:5,[0,3]]")
print(df.iloc[3:5,[0,3]])

header("8.df[Score<0.4]")
print(df[df.Score<0.4])


header("9.df['fullscore']=100")#create a new column
df['fullscore']=100*df.Score+df.sat
print df
'''

a1=0;a2=0;a3=0;a4=0
header("11.iterate rows of df with a for loop") #iterate rows
for index,row in df.iterrows():
    print index,row["sat"]
    if row["sat"]>80:
        a1=a1+1
    elif row["sat"]>60:
        a2=a2+1
    elif row["sat"]>40:
        a3=a3+1
    else:
        a4=a4+1

labels2= '>80', '60-80', '40-60','>40'
sizes2=[float(100*a1)/len(df.sat),float(100*a2)/len(df.sat),float(100*a3)/len(df.sat),float(100*a4)/len(df.sat)]
explode=(0,0.1,0,0)
plt.pie(sizes2,explode=explode,labels=labels2,autopct='%1.1f%%',shadow=True,startangle=270)
plt.axis('equal')
plt.title('sat score')
plt.show()