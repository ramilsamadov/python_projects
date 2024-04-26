# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:51:56 2024

@author: 48513
"""

from itertools import product

A = map(int,input().split())
B = map(int,input().split())

for i in sorted(tuple(product(A,B))):
    print(i,end=" ")