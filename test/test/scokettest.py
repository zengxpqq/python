#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *********************************
#
# author: xiangpeng zeng
#
# createtime: 2015-11-18 10:25:46 
#
# *********************************

print 'scoket test:'

import socket
import sys

localname = socket.gethostname()
print 'localname: ', localname

ip = socket.gethostbyname(socket.gethostname())
print 'ip: ', ip

if ip.startswith("127.") and os.name != "nt":
        for ifName in ["eth0","eth1","eth2"]:
            try:
                ip = getInterfaceIP(ifName)
                break
            except IOError:
                pass
print 'ip: ', ip                
                
print 'sys test:'
print sys.version
print sys.version_info
for x in range(len(sys.version_info)):
    print sys.version_info[x]                
