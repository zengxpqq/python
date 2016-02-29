#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-12 09:09:13  
#
# **************************************/

# f = open('/sw/ple/workspace/zengxp/test/file.py', 'w')

with open ('/sw/ple/workspace/zengxp/test/file.py', 'r') as f:
    for line in f.readlines():
        # strip(): 去掉字符串两边的空格
        # lstrip(): 去掉字符串左边的空格
        # rstrip(): 去掉字符串右边的空格
        print line.rstrip()
        
