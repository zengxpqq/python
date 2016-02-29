#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015.11.06  15:42:26
#
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

print '高阶函数'
def add(x, y ,f):
    return f(x) + f(y)

print add(-4, 5, abs)

print 'map'
def f(x):
    return x * x
print map(f, [1, 2, 3, 4])


print '过滤器'
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['a', '', 'b', None, ' '])



