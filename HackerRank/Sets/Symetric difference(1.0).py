# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:29:22 2024

@author: Samadov
"""
m,a=int(input()),input().split()
n,b=int(input()),input().split()
a_set=set(a)
b_set=set(b)
a_dif=a_set.difference(b_set)
b_dif=b_set.difference(a_set)
all_union=a_dif.union(b_dif)
print("\n".join(sorted(all_union,key=int)))
