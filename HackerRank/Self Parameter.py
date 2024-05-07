# -*- coding: utf-8 -*-
"""
Created on Tue May  7 02:20:05 2024

@author: Samadov
"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Ramil", 24)
p1.myfunc()