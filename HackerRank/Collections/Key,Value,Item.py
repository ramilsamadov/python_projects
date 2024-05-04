# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:41:58 2024

@author: Samadov
"""

from collections import defaultdict

d=defaultdict(list)

d["ad"].append("Ramil")
d["soyad"].append("Samadov")
for i in d.items():
    print(f"Collections Item: {i}")
    
    
for i in d.values():
    print(f"Collections Values: {i}")
    
    
for i in d.keys():
    print(f"Collections Keys: {i}")