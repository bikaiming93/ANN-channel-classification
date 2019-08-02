# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:25:33 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

case=[]
with open('example3.txt','r')as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for i in data:
        case.append(int(i[0]))