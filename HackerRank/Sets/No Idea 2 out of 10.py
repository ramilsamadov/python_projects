# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:41:52 2024

@author: Samadov
"""

arr_n = set(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

happiness = 0
for i in arr_n:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)


