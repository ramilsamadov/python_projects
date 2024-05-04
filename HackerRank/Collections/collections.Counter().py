# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:28:14 2024

@author: Samadov
"""

from collections import Counter
number_of_shoes=int(input())
shoe_size=list(map(int,input().split()))
earning=0
for i in range(int(input())):
    size,price=map(int,input().split())
    if size in shoe_size:
        earning+=price
        shoe_size.remove(size)
print(earning)