# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:45:13 2024

@author: Samadov
"""

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)