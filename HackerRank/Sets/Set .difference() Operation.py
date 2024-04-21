# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:25:18 2024

@author: Samadov
"""

count_en=int(input())
en_subs=set(map(int,input().split()))
count_fr=int(input())
fr_subs=set(map(int,input().split()))
len_dif=len(en_subs.difference(fr_subs))
print(len_dif)