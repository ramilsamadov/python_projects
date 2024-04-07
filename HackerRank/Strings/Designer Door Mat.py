# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:43:19 2024

@author: Samadov
"""

n,m=input().split()
n=int(n)
m=int(m)
for i in range(1,n//2 +1):
    x=".|."*(i*2 -1)
    print(x.center(m,"-"))
    
print("WELCOME".center(m,"-"))
    
for i in range(n//2 ,0, -1):
    x=".|."*(i*2 -1)
    print(x.center(m,"-"))
    
