# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:51:15 2024

@author: Samadov
"""

from itertools import product
a=set(map(int,input().split()))
a_list=list(a)
b=set(map(int,input().split()))
b_list=list(b)
num_product=product(a_list,b_list)
output = ' '.join([str(pair) for pair in num_product])
print(output)
