#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015.11.06  15:42:26
#
# Cteated on: 
# **************************************/


print 'list';

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
    
print L
print L[0:5]
print L[2:5]


l = [x * x for x in range(1, 11)]
print l

print range(1, 11)


l = [m + n for m in 'ABC' for n in 'XYZ']
print l

print '生成器'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fib(6):
    print n        
        


