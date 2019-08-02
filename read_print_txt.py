# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:54:54 2019

@author: 3784711
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

with open('example3.txt','r')as csvfile:
    for i in csv.reader(csvfile):
        print ','.join(i)
    print ''
