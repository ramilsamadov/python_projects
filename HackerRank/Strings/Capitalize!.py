# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:17:56 2024

@author: Samadov
"""


import math
import os
import random
import re
import sys

def solve(s):
    splitted = s.split(" ")
    listt = []
    boslug = " "
    for i in splitted:
        boyuk = i.capitalize()
        listt.append(boyuk)
    result = boslug.join(listt)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
