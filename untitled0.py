# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:15:21 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def header(msg):
    print('-'*50)
    print('['+msg+']')
    
filename = '5trainning_remove unknown data.csv'
df=pd.read_csv(filename)

a1=0;a2=0;a3=0;a4=0;a5=0;a6=0;a7=0
header("Channel distribution")

for index,row in df.iterrows():
    if row["channel_description"]=="Email":
        a1=a1+1
    elif row["channel_description"]=="Phone":
        a2=a2+1
    elif row["channel_description"]=="Fax/Mail":
        a4=a4+1
    elif row["channel_description"]=="IVR":
        a5=a5+1
    elif row["channel_description"]=="Online":
        a6=a6+1
    elif row["channel_description"]=="Web":
        a7=a7+1
    elif row["channel_description"]=="Web Servic":
        a7=a7+1
    else:
        a3=a3+1
        
print(a1+a2+a3+a4+a5+a6+a7)
        
labels2=  'Email(agent)','Web Chat (agent)', 'Phone (agent)','Fax/Mail (agent)','IVR (self)','Online (self)','Web Servic(agent)'
sizes2=[float(100*a1)/len(df.channel_description),float(100*a3)/len(df.channel_description),float(100*a2)/len(df.channel_description),float(100*a4)/len(df.channel_description),float(100*a5)/len(df.channel_description),float(100*a6)/len(df.channel_description),float(100*a7)/len(df.channel_description)]
print (sizes2)
explode=(0,0,0,0,0,0,0)
plt.pie(sizes2,explode=explode,labels=labels2,autopct='%1.1f%%',shadow=True,startangle=270)
plt.axis('equal')
plt.title('removed trainning data')
plt.show()
