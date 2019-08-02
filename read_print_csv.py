# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:36:10 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

#import csv data & display data
with open('example1.csv')as csvfile:
    for i in csv.reader(csvfile):
        print (','.join(i))
    print ('')

        