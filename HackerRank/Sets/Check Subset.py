# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:17:08 2024

@author: Samadov
"""

for i in range(int(input())):
    a1=int(input())
    a=set(map(int,input().split()))
    b1=int(input())
    b=set(map(int,input().split()))
    if a.issubset(b):
        print("True")
    else:
        print("False")


