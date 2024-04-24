# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 00:52:50 2024

@author: Samadov
"""

dividend=int(input())
divisor=int(input())
calc=divmod(dividend,divisor)
listt=list(calc)
print(listt[0])
print(listt[1])
print(calc)
