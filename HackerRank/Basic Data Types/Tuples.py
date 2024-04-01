# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:31:22 2024

@author: Samadov
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
