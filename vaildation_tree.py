# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:43:46 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def header(msg):
    print('-'*50)
    print('['+msg+']')
    
filename = 'Pickup.csv'
df=pd.read_csv(filename)



sample=df
#sample2=sample1[pd.to_numeric(sample1.Weight)<=50]
#sample2=sample1[pd.to_numeric(sample1.Package_Dimension)>=3000]
#sample=sample1[pd.to_numeric(sample1.Package_Dimension)>=10000]



a1=0;a2=0;a3=0;a4=0;a5=0;a6=0;a7=0;a8=0
header("Channel distribution")

for index,row in sample.iterrows():
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
    if row["DIFF"]==0:
        a8=a8+1

        
labels2=  'Email(agent)','Web Chat (agent)', 'Phone (agent)','Fax/Mail (agent)','IVR (self)','Online (self)','Web Servic(agent)'
sizes2=[float(100*a1)/len(sample.Sat),float(100*a3)/len(sample.Sat),float(100*a2)/len(sample.Sat),float(100*a4)/len(sample.Sat),float(100*a5)/len(sample.Sat),float(100*a6)/len(sample.Sat),float(100*a7)/len(sample.Sat)]

explode=(0,0,0,0,0,0,0)
plt.pie(sizes2,explode=explode,labels=labels2,autopct='%1.1f%%',shadow=True,startangle=270)
plt.axis('equal')
plt.title('Pickup in validation"')
plt.show() 

'''
sizes1= [4.2249546287371595, 0.018235340089092663, 54.18457637568274, 0.274398450864442, 4.871875027135923, 32.307812540703885, 4.11814763678676]

sizes3=[0,0,0,0,0,0,0]
for i in range(7):
    sizes3[i]=sizes2[i]-sizes1[i]


print(np.std(sizes3))

print(sizes2)
'''
print(a1+a2+a3+a4+a5+a6+a7)
print(a8)
print(a8/(a1+a2+a3+a4+a5+a6+a7))

      


