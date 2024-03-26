# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:22:49 2024

@author: Samadov
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif n%2==0:
        print("Not Weird")
