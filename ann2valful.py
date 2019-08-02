# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:13:23 2019

@author: 3784711
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:35:09 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import random
from tensorflow.keras import layers

Phone,Online,IVR,Web_Servic=[],[],[],[]
SHP_Time,Package_Dimension,Weight=[],[],[]
SHP_PCE_QTY,Express,Ground,Home_Del,Morning,Afternoon,Night=[],[],[],[],[],[],[]
Late_Night,Ship4,Ship5,Ship6,Ship7,Ship810,Dest4,Dest5,Dest6,Dest7=[],[],[],[],[],[],[],[],[],[]
Dest810,Ship_Time,Del_Time,Case_Date,RB,RR,RM,RU,RW,Payer=[],[],[],[],[],[],[],[],[],[]
with open('unlabeled2.csv')as csvfile:    
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
         Phone.append(int(i[0]))
         Online.append(int(i[1]))
         IVR.append(int(i[2]))
         Web_Servic.append(int(i[3]))
         SHP_Time.append(float(i[4]))
         Package_Dimension.append(int(i[5]))
         Weight.append(float(i[6]))
         SHP_PCE_QTY.append(int(i[7]))
         Express.append(int(i[8]))
         Ground.append(int(i[9]))
         Home_Del.append(int(i[10]))
         Morning.append(int(i[11]))
         Afternoon.append(int(i[12]))
         Night.append(int(i[13]))
         Late_Night.append(int(i[14]))
         Ship4.append(int(i[15]))
         Ship5.append(int(i[16]))
         Ship6.append(int(i[17]))
         Ship7.append(int(i[18]))
         Ship810.append(int(i[19]))
         Dest4.append(int(i[20]))
         Dest5.append(int(i[21]))
         Dest6.append(int(i[22]))
         Dest7.append(int(i[23]))
         Dest810.append(int(i[24]))
         Ship_Time.append(int(i[25]))
         Del_Time.append(int(i[26]))
         Case_Date.append(int(i[27]))
         RB.append(int(i[28]))
         RR.append(int(i[29]))
         RM.append(int(i[30]))
         RU.append(int(i[31]))
         RW.append(int(i[32]))
         Payer.append(int(i[33]))
         
y=np.column_stack((Phone,Online,IVR,Web_Servic))
x=np.column_stack((SHP_Time,Package_Dimension,Weight,SHP_PCE_QTY,Express,Ground,Home_Del,Morning,Afternoon,Night,Late_Night,Ship4,Ship5,Ship6,Ship7,Ship810,Dest4,Dest5,Dest6,Dest7,Dest810,Ship_Time,Del_Time,Case_Date,RB,RR,RM,RU,RW,Payer))


tPhone,tOnline,tIVR,tWeb_Servic=[],[],[],[]
tSHP_Time,tPackage_Dimension,tWeight=[],[],[]
tSHP_PCE_QTY,tExpress,tGround,tHome_Del,tMorning,tAfternoon,tNight=[],[],[],[],[],[],[]
tLate_Night,tShip4,tShip5,tShip6,tShip7,tShip810,tDest4,tDest5,tDest6,tDest7=[],[],[],[],[],[],[],[],[],[]
tDest810,tShip_Time,tDel_Time,tCase_Date,tRB,tRR,tRM,tRU,tRW,tPayer=[],[],[],[],[],[],[],[],[],[]
with open('ann2valful.csv')as csvfile:    
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
         tPhone.append(int(i[0]))
         tOnline.append(int(i[1]))
         tIVR.append(int(i[2]))
         tWeb_Servic.append(int(i[3]))
         tSHP_Time.append(float(i[4]))
         tPackage_Dimension.append(int(i[5]))
         tWeight.append(float(i[6]))
         tSHP_PCE_QTY.append(int(i[7]))
         tExpress.append(int(i[8]))
         tGround.append(int(i[9]))
         tHome_Del.append(int(i[10]))
         tMorning.append(int(i[11]))
         tAfternoon.append(int(i[12]))
         tNight.append(int(i[13]))
         tLate_Night.append(int(i[14]))
         tShip4.append(int(i[15]))
         tShip5.append(int(i[16]))
         tShip6.append(int(i[17]))
         tShip7.append(int(i[18]))
         tShip810.append(int(i[19]))
         tDest4.append(int(i[20]))
         tDest5.append(int(i[21]))
         tDest6.append(int(i[22]))
         tDest7.append(int(i[23]))
         tDest810.append(int(i[24]))
         tShip_Time.append(int(i[25]))
         tDel_Time.append(int(i[26]))
         tCase_Date.append(int(i[27]))
         tRB.append(int(i[28]))
         tRR.append(int(i[29]))
         tRM.append(int(i[30]))
         tRU.append(int(i[31]))
         tRW.append(int(i[32]))
         tPayer.append(int(i[33]))
         
yt=np.column_stack((tPhone,tOnline,tIVR,tWeb_Servic))
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
y_train=np.reshape(y_train,(len(y_train),4))

print(np.shape(y_train))
print(np.shape(x_train))
print(np.shape(x_valid))
print(np.shape(y_valid))

x_train=tf.keras.utils.normalize(x_train,axis=1) #normalization
x_valid=tf.keras.utils.normalize(x_valid,axis=1)
y_train=tf.keras.utils.normalize(y_train,axis=1) #normalization
y_valid=tf.keras.utils.normalize(y_valid,axis=1)


inputs=inputs = tf.keras.Input(shape=(30,))
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(128, activation='relu')(x)
predictions = layers.Dense(4, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=predictions)

model.compile(optimizer=tf.train.RMSPropOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=22)
model.summary()

print(np.shape(yt))
print(np.shape(xt))

predictions = model.predict(xt)
predictions=np.reshape(predictions,(len(predictions),4))

print(np.shape(predictions))

count=0
count2=0
count3=0
count4=0
count5=0
for i in range(len(predictions)):
    sq=(predictions[i,0]-yt[i,0])**2+(predictions[i,1]-yt[i,1])**2+(predictions[i,2]-yt[i,2])**2+(predictions[i,3]-yt[i,3])**2
    if sq<0.00000001:
        count=count+1
    if predictions[i,0]>0.9:
        count2=count2+1
    if predictions[i,1]>0.9:
        count3=count3+1
    if predictions[i,2]>0.9:
        count4=count4+1
    if predictions[i,3]>0.9:
        count5=count5+1

print(count/len(predictions))
print(count2)
print(count3)
print(count4)
print(count5)     