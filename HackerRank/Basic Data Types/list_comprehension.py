# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:57:06 2024

@author: Samadov
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    listt=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k !=n):
                    listt.append([i,j,k])
    print(listt)
