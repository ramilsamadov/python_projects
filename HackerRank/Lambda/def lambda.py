# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:01:27 2024

@author: Samadov
"""
def MyFunc(n):
    return lambda a: a*n

y=MyFunc(10)
print(y(5))