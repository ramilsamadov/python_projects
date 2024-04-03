# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:43:02 2024

@author: Samadov
"""

def swap_case(s):
    word_update=""
    for word in s:
        if word.isupper():
            word_update+=word.lower()
        elif word.islower():
            word_update+=word.upper()
        else:
            word_update+=word
            
    return word_update

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)