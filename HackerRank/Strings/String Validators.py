# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:48:26 2024

@author: Samadov
"""

if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    
    print(any(c.isalpha() for c in s))
    
    print(any(c.isdigit() for c in s))
    

    print(any(c.islower() for c in s))
    

    print(any(c.isupper() for c in s))
