#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************
#
# Author: xiangpeng zeng
# 
# Create on: 2015-11-19 09:12:37 
#
# ********************************


import os
import sys
try:
    import qb
except:
    if 'QBDIR' in os.environ:
        QBDIR = os.environ['QBDIR']
    else:
        if os.name == 'posix':
            if os.uname()[0] == 'Darwin':
                QBDIR = '/Applications/pfx/qube'
            else:
                QBDIR = '/usr/local/pfx/qube'

    sys.path.append('%s/api/python' % QBDIR)
    import qb
    
print qb.QB_API_XML  
print qb.QB_API_BINARY
print qb.QB_TIME_EPOCH_OFFSET
print qb.QB_CLIENT_DEFAULT_CONF  

print qb.hostinfo()[0]
