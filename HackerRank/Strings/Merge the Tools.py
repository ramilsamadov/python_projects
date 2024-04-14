# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:07:57 2024

@author: Samadov
"""

def merge_the_tools(string, k):
    new_string=""
    for i in range(0,len(string),k):
        
        for letter in string[i:i+k]:
            if letter not in new_string:
                new_string=new_string+letter
        print(new_string)
        new_string=""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)