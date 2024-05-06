# -*- coding: utf-8 -*-
"""
Created on Tue May  7 01:53:22 2024

@author: Samadov
"""

class MyClass:
    def __init__(a,b,c):
        a.name=b
        a.surname=c
        
    def __str__(a):
        return f"{a.name} {a.surname}"
    
y=MyClass("Ramil", "Samadov")
print(y)    

