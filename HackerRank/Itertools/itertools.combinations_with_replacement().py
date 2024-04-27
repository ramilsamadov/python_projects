# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:26:05 2024

@author: Samadov
"""

from itertools import combinations_with_replacement

string, length = input().split()
length = int(length)

for j in combinations_with_replacement(sorted(string),length):
    print("".join(j))
