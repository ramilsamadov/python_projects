# -*- coding: utf-8 -*-
"""
Created on Tue May  7 01:36:55 2024

@author: Samadov
"""

class MyClass:
    def __init__(a,b,c):
        a.name=b
        a.surname=c
n_s=MyClass("Ramil", "Samadov")
print(n_s.name +" "+n_s.surname)