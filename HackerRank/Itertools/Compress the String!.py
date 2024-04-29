# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:28:38 2024

@author: Samadov
"""

from itertools import groupby
x=input()
listt=[]
for key,group in groupby(x):
    length=len(list(group)),int(key)
    count=listt.append(length)

for i in listt:
    print("({}, {})".format(i[0], i[1]),end=" ")
    
