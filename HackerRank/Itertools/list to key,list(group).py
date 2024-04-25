# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 01:20:53 2024

@author: Samadov
"""

import itertools
x=[
   {"city":"warsaw","name":"ramil","age":24},
   {"city":"baku","name":"famil","age":23}
   ]
z=x.sort(key=lambda  y: y["city"])
for key,group in itertools.groupby(x, key=lambda y: y["city"]):
    print(key,list(group))
    