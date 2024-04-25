# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 01:13:49 2024

@author: Samadov
"""

import itertools
x="RRRRAAAMMMIIILLL"
for key,group in itertools.groupby(x):
    print(key,list(group))