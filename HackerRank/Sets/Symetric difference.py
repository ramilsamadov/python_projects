# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:29:22 2024

@author: Samadov
"""

m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
sortedd=sorted((a-b).union(b-a))
for i in sortedd:
    print(i)
