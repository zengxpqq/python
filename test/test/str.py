#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015.11.06  15:42:26
#
# Cteated on: 
# **************************************/


print '统计字符串个数';

str = raw_input('输入一行字符串：')
n = len(str)

alpha = 0
digit = 0
space = 0
others = 0

for i in range(n):
    if str[i].isalpha():
        alpha = alpha + 1
    elif str[i].isdigit():
        digit = digit + 1
    elif str[i].isspace():
        space += 1
    else:
        others += 1
    
print '字符串个数为:', n 
print '字母个数为：', alpha
print '数字个数为：', digit
print '空格个数为：', space      
print '其他个数为：', others









