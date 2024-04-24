# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:20:03 2024

@author: Samadov
"""

import math 
ab=int(input())
bc=int(input())
ac=math.sqrt(ab**2 + bc**2)
angle=math.degrees(math.asin(ab/ac))
print(round(angle),end='\u00b0')