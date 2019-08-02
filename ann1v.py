# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:15:45 2019

@author: 3784711
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 09:24:09 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import random
from tensorflow.keras import layers

Phone,Email,Web=[],[],[]
SHP_Time,Package_Dimension,Weight=[],[],[]
SHP_PCE_QTY,Express,Ground,Home_Del,Morning,Afternoon,Night=[],[],[],[],[],[],[]
Late_Night,Ship4,Ship5,Ship6,Ship7,Ship810,Dest4,Dest5,Dest6,Dest7=[],[],[],[],[],[],[],[],[],[]
Dest810,Ship_Time,Del_Time,Case_Date,RB,RR,RM,RU,RW,Payer=[],[],[],[],[],[],[],[],[],[]
with open('9ship_alluse.csv')as csvfile:    
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
         Phone.append(int(i[0]))
         Email.append(int(i[1]))
         Web.append(int(i[2]))
         SHP_Time.append(float(i[3]))
         Package_Dimension.append(int(i[4]))
         Weight.append(float(i[5]))
         SHP_PCE_QTY.append(int(i[6]))
         Express.append(int(i[7]))
         Ground.append(int(i[8]))
         Home_Del.append(int(i[9]))
         Morning.append(int(i[10]))
         Afternoon.append(int(i[11]))
         Night.append(int(i[12]))
         Late_Night.append(int(i[13]))
         Ship4.append(int(i[14]))
         Ship5.append(int(i[15]))
         Ship6.append(int(i[16]))
         Ship7.append(int(i[17]))
         Ship810.append(int(i[18]))
         Dest4.append(int(i[19]))
         Dest5.append(int(i[20]))
         Dest6.append(int(i[21]))
         Dest7.append(int(i[22]))
         Dest810.append(int(i[23]))
         Ship_Time.append(int(i[24]))
         Del_Time.append(int(i[25]))
         Case_Date.append(int(i[26]))
         RB.append(int(i[27]))
         RR.append(int(i[28]))
         RM.append(int(i[29]))
         RU.append(int(i[30]))
         RW.append(int(i[31]))
         Payer.append(int(i[32]))

y=np.column_stack((Phone,Email,Web))
x=np.column_stack((SHP_Time,Package_Dimension,Weight,SHP_PCE_QTY,Express,Ground,Home_Del,Morning,Afternoon,Night,Late_Night,Ship4,Ship5,Ship6,Ship7,Ship810,Dest4,Dest5,Dest6,Dest7,Dest810,Ship_Time,Del_Time,Case_Date,RB,RR,RM,RU,RW,Payer))

tPhone,tEmail,tWeb=[],[],[]
tSHP_Time,tPackage_Dimension,tWeight=[],[],[]
tSHP_PCE_QTY,tExpress,tGround,tHome_Del,tMorning,tAfternoon,tNight=[],[],[],[],[],[],[]
tLate_Night,tShip4,tShip5,tShip6,tShip7,tShip810,tDest4,tDest5,tDest6,tDest7=[],[],[],[],[],[],[],[],[],[]
tDest810,tShip_Time,tDel_Time,tCase_Date,tRB,tRR,tRM,tRU,tRW,tPayer=[],[],[],[],[],[],[],[],[],[]
with open('ann1valful.csv')as csvfile:    
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
         tPhone.append(int(i[0]))
         tEmail.append(int(i[1]))
         tWeb.append(int(i[2]))
         tSHP_Time.append(float(i[3]))
         tPackage_Dimension.append(int(i[4]))
         tWeight.append(float(i[5]))
         tSHP_PCE_QTY.append(int(i[6]))
         tExpress.append(int(i[7]))
         tGround.append(int(i[8]))
         tHome_Del.append(int(i[9]))
         tMorning.append(int(i[10]))
         tAfternoon.append(int(i[11]))
         tNight.append(int(i[12]))
         tLate_Night.append(int(i[13]))
         tShip4.append(int(i[14]))
         tShip5.append(int(i[15]))
         tShip6.append(int(i[16]))
         tShip7.append(int(i[17]))
         tShip810.append(int(i[18]))
         tDest4.append(int(i[19]))
         tDest5.append(int(i[20]))
         tDest6.append(int(i[21]))
         tDest7.append(int(i[22]))
         tDest810.append(int(i[23]))
         tShip_Time.append(int(i[24]))
         tDel_Time.append(int(i[25]))
         tCase_Date.append(int(i[26]))
         tRB.append(int(i[27]))
         tRR.append(int(i[28]))
         tRM.append(int(i[29]))
         tRU.append(int(i[30]))
         tRW.append(int(i[31]))
         tPayer.append(int(i[32]))
yt=np.column_stack((tPhone,tEmail,tWeb))
xt=np.column_stack((tSHP_Time,tPackage_Dimension,tWeight,tSHP_PCE_QTY,tExpress,tGround,tHome_Del,tMorning,tAfternoon,tNight,tLate_Night,tShip4,tShip5,tShip6,tShip7,tShip810,tDest4,tDest5,tDest6,tDest7,tDest810,tShip_Time,tDel_Time,tCase_Date,tRB,tRR,tRM,tRU,tRW,tPayer))

x_train,y_train,x_valid,y_valid=[],[],[],[]
for i in range(len(x)):
    if random.uniform(0,1)>0.7:
        y_train.append([y[i,:]])
        x_train.append([x[i,:]])
    else:
        y_valid.append([y[i,:]])
        x_valid.append([x[i,:]])

x_train=np.reshape(x_train,(len(x_train),30))
y_train=np.reshape(y_train,(len(y_train),3))

print(np.shape(y_train))
print(np.shape(x_train))
print(np.shape(x_valid))
print(np.shape(y_valid))




x_train=tf.keras.utils.normalize(x_train,axis=1) #normalization
x_valid=tf.keras.utils.normalize(x_valid,axis=1)
y_train=tf.keras.utils.normalize(y_train,axis=1) #normalization
y_valid=tf.keras.utils.normalize(y_valid,axis=1)     


'''
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))  
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu)) 
model.add(tf.keras.layers.Dense(y.shape[1],activation=tf.nn.softmax)) 

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=50)
'''

inputs=inputs = tf.keras.Input(shape=(30,))
x = layers.Dense(32, activation='relu')(inputs)
x = layers.Dense(32, activation='relu')(x)
predictions = layers.Dense(3, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=predictions)

model.compile(optimizer=tf.train.RMSPropOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=20)
model.summary()

print(np.shape(yt))
print(np.shape(xt))

predictions = model.predict(xt)
predictions=np.reshape(predictions,(len(predictions),3))

print(np.shape(predictions))

#print(yt[0])
count=0
count2=0
for i in range(len(predictions)):
    sq=(predictions[i,0]-yt[i,0])**2+(predictions[i,1]-yt[i,1])**2+(predictions[i,2]-yt[i,2])**2
    if sq<0.00000001:
        count=count+1
#    if predictions[i,0]<0.995:
#        count2=count2+1

print(count/len(predictions))
#print(count2)