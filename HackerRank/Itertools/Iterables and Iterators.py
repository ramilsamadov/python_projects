# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:26:11 2024

@author: Samadov
"""

from itertools import combinations
n=int(input())
listt=list(input().split())
k=int(input())
comb=list(combinations(listt,k))
r=[i for i in comb if 'a' in i]
print(len(r)/len(comb))
