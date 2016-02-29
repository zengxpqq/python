#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************
#
# Author: xiangpeng zeng
# 
# Create on: 2015-11-19 16:15:27 
#
# ********************************

print 'current time:'

import time
import os

current = time.ctime()
print current

print time.time()
print time.localtime()
print time.localtime().tm_hour
'''
while True:
    if time.localtime().tm_hour < 11:
        if time.localtime().tm_min < 55:
            os.system('python /job/HOME/zengxp/桌面/12.py')
'''
while True:
    if time.localtime().tm_hour < 21:
        #if time.localtime().tm_min < 30:
            os.system('python /job/HOME/zengxp/桌面/enlargetwo.py')
  
