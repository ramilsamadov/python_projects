# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:20:50 2024

@author: Samadov
"""

from itertools import product

k,m=list(map(int,input().split()))
listt=[]
for i in range(k):
    listt.append(list(map(int,input().split()))[1:])
    
list_product=list(product(*listt))

final=[]
for j in list_product:
    total=0
    for k in j:
        total=total+k**2
    final.append(total%m)
print(max(final))
    
