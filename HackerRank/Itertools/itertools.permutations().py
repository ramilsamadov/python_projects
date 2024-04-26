# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:54:48 2024

@author: Samadov
"""

from itertools import permutations
inputt=input().split()
string,length=inputt[0],int(inputt[1])
[print("".join(i)) for i in sorted(list(permutations(string,length)))]
