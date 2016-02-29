#!/usr/bin/env python
# -*- coding: utf-8 -*-
#************************************
#
# Author: xiangpeng zeng
#
# Create time: 2015-11-25 15:59:41
#
#************************************

'''
   check the Workers state
'''

import sys
import os
import re 
sys.path.append('/usr/local/pfx/qube/api/python')
import qb
sys.path.append('/sw/ple/studio/lib')
import bcommunication.base_message as baseMessage
import bcommunication.base_email as baseemail
ACCOUNT = 'qubeinfo'
PASSWORD = 'J4GRB@1g'

running = qb.jobinfo(status = 'running')[0]['hosts']
worker = [running]


rough_works = list()

rough_works = [qb.jobinfo(status = "running")[0]['hosts']]
for items in rough_works:
    items = items.split(',')

    while '' in items:
        items.remove('')
#print items
def jobstatus():
    for i in range(len(qb.jobinfo(status = 'running'))):
        print qb.jobinfo(status = 'running')[i]['id']
        print qb.jobinfo(status = 'running')[i]


def search_down():
    for i in range(len(qb.hostinfo(state = 'down'))):
        node = re.compile(r'^[node]|^[NODE]')
        if node.match(qb.hostinfo(state = 'down')[i]['name']):            
            content = qb.hostinfo(state = 'down')[i]['name']
            print content
            baseMessage.send('zengxp', content, account=ACCOUNT, password=PASSWORD )
search_down()


#print qb.Job['id']


























# 题目名称 题目类型 题目来源 校外指导老师名称 职称 学历 电话
# 美丽厦门 视频   主管  张凯华   流程技术指导 本科 1348 866 7489
    
  



