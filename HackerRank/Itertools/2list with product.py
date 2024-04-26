# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:37:12 2024

@author: Samadov
"""

from itertools import product
def pr(ar1,ar2):
    return(list(product(ar1,ar2)))

ar1=[1,2,3,4]
ar2=[5,6,7]

print(pr(ar1,ar2))
