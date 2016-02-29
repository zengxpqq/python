#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Create on: 2015-11-07 12:15:47 
#
# **************************************/

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print calc(1, 2 ,3)
