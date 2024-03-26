# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:28:10 2024

@author: Samadov
"""

def is_leap(year):
    leap = False
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
    
    return leap

year = int(input())
print(is_leap(year))