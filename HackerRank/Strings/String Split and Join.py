# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:44:21 2024

@author: Samadov
"""

def split_and_join(line):
    return line.replace(" ","-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)