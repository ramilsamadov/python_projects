# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:36:05 2024

@author: Samadov
"""

def print_rangoli(size):
    alphabet=[chr(i) for i in range(97,123)]
    alphabet=alphabet[:size]
    indices=list(range(size))
    indices=indices[:-1]+indices[::-1]
    for i in indices:
        start_index=i+1
        original=alphabet[-start_index:]
        reverse=original[::-1]
        row=reverse+original[1:]
        row="-".join(row)
        width=size*4-3
        row=row.center(width,"-")
        
        print(row)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)