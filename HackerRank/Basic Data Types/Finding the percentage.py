# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:24:29 2024

@author: Samadov
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    hesabla = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{hesabla:.2f}")

