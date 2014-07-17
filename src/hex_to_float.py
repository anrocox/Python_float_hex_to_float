#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

In Python how to convert a hexadecimal string to float?

En Python ¿Cómo convertir un string hexadecimal a float?
'''

#create a string with a number in hexadecimal format
s = '11B.DF7CED917'
print(s)

#fromhex() class method return the float represented by a hexadecimal string
#https://docs.python.org/3/library/stdtypes.html#float.fromhex
f = float.fromhex(s)
print(type(f))
print(f)

#create a string with a negative number in hexadecimal format
s = '-96F5.5D0E56042'
print(s)

#convert the hex string 's' to float
f = float.fromhex(s)
print(f)
