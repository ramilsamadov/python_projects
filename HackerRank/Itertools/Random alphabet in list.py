# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:12:19 2024

@author: Samadov
"""

import string,random,itertools

asci=string.ascii_lowercase
y=list(itertools.compress(asci,[random.randint(0, 1) for _ in range(len(asci))]))
print(y)