# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:17:35 2024

@author: Samadov
"""
def average(array):
    
    unique_heights = set(array)
    total_height = sum(unique_heights)
    number_of_plants = len(unique_heights)
    average_height = total_height / number_of_plants
    return average_height


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

