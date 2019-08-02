# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:05:10 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

clbk1,clbk2,clbk3,score,close=[],[],[],[],[]
with open('example2.csv')as csvfile:
    data=csv.reader(csvfile,delimiter=',')
#    df = pd.DataFrame(data)
    for i in data:
        clbk1.append(int(i[2]))
        clbk2.append(int(i[3]))
        clbk3.append(int(i[4]))
        score.append(float(i[29]))
        close.append(str(i[7]))
#    print 'clbk1 {}, clbk2 {}, clbk3 {}'.format(clbk1,clbk2,clbk3)
#print df['0']

    
a1=0;a2=0;b1=0;b2=0;b3=0;b4=0;c1=0;c2=0;c3=0;c4=0;

for i in range(len(clbk3)):
    if clbk3[i]==1:
        a1=a1+1
    else:
        a2=a2+1
print (a1,a2)

for i in range(len(score)):
    if score[i]>80:
        b1=b1+1
    elif score[i]>60:
        b2=b2+1
    elif score[i]>40:
        b3=b3+1
    else:
        b4=b4+1
print (b1,b2,b3,b4)
        
for i in range(len(close)):
    if "01" in close[i]: 
        c1=c1+1
    elif "CLOSED" in close[i]:
        c2=c2+1
    elif "LETTER" in close[i]:
        c3=c3+1
    else:
        c4=c4+1
print (c1,c2,c3,c4)    
        
        

labels= 'Require Call Back','No Requires'
sizes=[float(100*a1)/len(clbk3),float(100*a2)/len(clbk3)]

plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()

labels2= '>80', '60-80', '40-60','>40'
sizes2=[float(100*b1)/len(score),float(100*b2)/len(score),float(100*b3)/len(score),float(100*b4)/len(score)]
explode=(0,0.1,0,0)

plt.pie(sizes2,explode=explode,labels=labels2,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()

labels3= 'NO CREDIT & REFUND', 'CLOSED', 'LETTER SENT','others'
sizes3=[float(100*c1)/len(score),float(100*c2)/len(score),float(100*c3)/len(score),float(100*c4)/len(score)]
explode=(0.1,0,0,0)

plt.pie(sizes3,explode=explode,labels=labels3,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()

 


        