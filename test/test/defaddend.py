#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Create on: 2015-11-07 12:15:47 
#
# **************************************/

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
    

print add_end([1, 2 ,3])
