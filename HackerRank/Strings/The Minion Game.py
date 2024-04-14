# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:32:37 2024

@author: Samadov
"""

def minion_game(string):
    length=len(string)
    con=0
    vow=0
    for i in range(length):
        if string[i] in "AEIOU":
            vow=vow+(length-i)
        else:
            con=con+(length-i)
    if con>vow:
        print("Stuart {}".format(con))
    elif con==vow:
        print("Draw")
    else:
        print("Kevin {}".format(vow))

if __name__ == '__main__':
    s = input()
    minion_game(s)