# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:59:37 2024

@author: Samadov
"""

K=int(input())
groups=input().split()
set1=set()
set2=set()
for i in groups:
    if i not in set1:
        set1.add(i)
        set2.add(i)
    else:
        set2.discard(i)
print(set2.pop())