# -*- coding: utf-8 -*-
"""
Created on Tue May  7 02:07:51 2024

@author: Samadov
"""
class MyClass:
    def __init__(a,b,c):
        a.name=b
        a.surname=c
    def myfunction(a):
        print("Hello my name is "+a.name)
y=MyClass("Ramil", "Samadov")
y.myfunction()
