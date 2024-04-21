# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:13:42 2024

@author: Samadov
"""

count_en_subs=int(input())
set_en_subs=set(map(int,input().split()))
count_fr_subs=int(input())
set_fr_subs=set(map(int,input().split()))
print(len(set_en_subs.union(set_fr_subs)))
