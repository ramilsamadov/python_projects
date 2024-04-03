# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:46:50 2024

@author: Samadov
"""

def mutate_string(string, position, character):
    listed_s=list(string)
    listed_s[position]=character
    string="".join(listed_s)    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)