# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 01:14:32 2024

@author: Samadov
"""

from itertools import combinations
string,length=input().split()
length=int(length)
for i in range(1,length+1):
    for j in combinations(sorted(string),i):
        print("".join(j))