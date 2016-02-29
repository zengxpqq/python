#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
#
# Created time: 2015-11-28 11:30:08 
#
# **************************************/

import os
print 'node number range is 467~566'
#print 'ip number range is 145~244'
#ip = raw_input("you need connect windows ip is : 172.16.40.")
#print 'ip : 172.16.40.' + ip


#os.system('rdesktop 172.16.40.' + ip + ' -u ad\renderslavexm -p bfx420f')

#os.system('rdesktop 172.16.40.' + ip )

'''
nodes = raw_input("nodes number: ")
list = nodes.split(',')
print list
print len(list)
for i in list:
    print i
'''
import sys,time

for i in range(5):
    sys.stdout.write('{0}/5r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)
    
print '\n'
for i in range(5):
    sys.stdout.write(str(i+1)*(i+1) + '\r')
    sys.stdout.flush()
    time.sleep(1)

for i in range(5):
    sys.stdout.write('' * 10 + '\r')
    sys.stdout.flush()
    sys.stdout.write(str(i+1)*(i+1) + '\r')
    sys.stdout.flush()
    time.sleep(1)

class ProgressBar:
    def __init__(self,count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    
    def move(self):
        self.count += 1
        
    def log(self, s):
        sys.stdout.write('' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}:'.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
        
bar = ProgressBar(total = 10)
    
for i in range(10):
    bar.move()
    bar.log('we have arrived at:' + str(i + 1))
    time.sleep(1)
                         
    






















