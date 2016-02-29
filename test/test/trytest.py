#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-11 13:42:57 
#
# **************************************/


print '异常处理';

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except StandardError, e:
    print 'except:', e 
    raise ValueError('input error')
except ZeroDivisionError, e:
    print 'except:', e
   
finally:
    print 'finally...'
print 'END'        



