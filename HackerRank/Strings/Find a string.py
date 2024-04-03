# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:47:26 2024

@author: Samadov
"""

def count_substring(string, sub_string):
    count = 0
    length = len(string)
    sub_length = len(sub_string)
    
    for i in range(length - sub_length + 1):
        if string[i:i+sub_length] == sub_string:
            count += 1
    
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)