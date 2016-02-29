#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-09 08:56:19 
#
# Cteated on: 
# **************************************/


print 'hello world';

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print power(5)
print power(6, 3)


