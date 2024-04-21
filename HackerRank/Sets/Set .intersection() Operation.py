# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:19:10 2024

@author: Samadov
"""

count_en_subs=int(input())
en_subs=set(map(int,input().split()))
count_fr_subs=int(input())
fr_subs=set(map(int,input().split()))
len_of_both=len(en_subs.intersection(fr_subs))
print(len_of_both)
