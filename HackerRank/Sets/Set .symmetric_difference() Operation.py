# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:34:20 2024

@author: Samadov
"""

count_en=int(input())
en_subs=set(map(int,input().split()))
count_fr=int(input())
fr_subs=set(map(int,input().split()))
len_subs=len((en_subs - fr_subs)^(fr_subs - en_subs))
print(len_subs)

