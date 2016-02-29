#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015.11.06  15:42:26
#
# Cteated on: 
# **************************************/


print 'hello world';

import os
import time
'''
print os.getcwd()
while True:
    for i in range(10):
        print i
        if i > 6:
            break
    time.sleep(1) 
'''

HOSTSTATUS = 'active'
import sys
sys.path.append('/usr/local/pfx/qube/api/python')
import qb
 

while True:
    hostInfos = qb.hostinfo(state=HOSTSTATUS)
    print '[%s]' % time.strftime('%Y-%m-%d %H:%M:%S'), 'server started.'
    for singlehost in hostInfos:
        if singlehost['groups'] == '':
            os.system('qbadmin w --reconfigure')
            break
        
    time.sleep(120)
    


