# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:22:15 2024

@author: Samadov
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(sorted(set(arr), reverse=True)[1])
