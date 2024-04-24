# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:25:48 2024

@author: Samadov
"""

from cmath import polar
complex_num=complex(input())
polar_form=polar(complex_num)

for i in polar_form:
    print(i)
