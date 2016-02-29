#!/usr/bin/env python

#https://github.com/NARKOZ/hacker-scripts

import sys
import os
import time
import re 
sys.path.append('/usr/local/pfx/qube/api/python')
import qb
sys.path.append('/sw/ple/studio/lib')
import bcommunication.base_message as baseMessage
import bcommunication.base_email as baseemail
import getpass
NAME = getpass.getuser()
ACCOUNT = 'qubeinfo'
PASSWORD = 'J4GRB@1g'

def hython():
    while 1:
        name = re.compile(r'[cwb0320]|[cwb0380]|[cwb0390]')        
        for i in range(len(qb.jobinfo(status = 'running'))):
            if name.search(qb.jobinfo(status = 'running')[i]['name']):
                mission.append(qb.jobinfo(status = 'running')[i]['name'])
                print qb.jobinfo(status = 'running')[i]['name']
                print qb.jobinfo(status = 'running')[i]['priority']
            
        print '\n' 
        time.sleep(10)
    
def nuke():
    while 1:
        name = re.compile(r'[n]')
        try :
            for i in range(len(qb.jobinfo(status = 'running'))):
                if name.match(qb.jobinfo(status = 'running')[i]['name']):

                    if qb.jobinfo(status = 'running')[i]['cpus'] != qb.jobinfo(status = 'running')[i]['todo']:
                        if qb.jobinfo(status = 'running')[i]['todo'] < 200:                            
                            qb.modify({'cpus': qb.jobinfo(status = 'running')[i]['todo']}, qb.jobinfo(status = 'running')[i]['id'])
                        else:
                            pass
                            qb.modify({'cpus': 200}, qb.jobinfo(status = 'running')[i]['id'])
                    #content = qb.jobinfo(status = 'running')[i]['user'] + '  ' + str(qb.jobinfo(status = 'running')[i]['todo'])
                    #if str(qb.jobinfo(status = 'running')[i]['todo']) >= 200:
                        #baseMessage.send('zengxp', content, account=ACCOUNT, password=PASSWORD )
        except IndexError :
            print 'cuole'
        time.sleep(10)
                
nuke()
        
def find_nuke():
    
        name = re.compile(r'[n]')

        for i in range(len(qb.jobinfo(status = 'running'))):
            #print qb.jobinfo(status = 'running')[i]['name']
            if name.match(qb.jobinfo(status = 'running')[i]['name']):
                print  str(i) + '  ' +  qb.jobinfo(status = 'running')[i]['name']
                #print qb.jobinfo(status = 'running')[i]['name']
                content = qb.jobinfo(status = 'running')[i]['user'] + ' ' + str(qb.jobinfo(status = 'running')[i]['todo'])
                baseMessage.send(NAME, content, account=ACCOUNT, password=PASSWORD )
            else:
                print 'pass' + '  ' + str(i) + '  ' + qb.jobinfo(status = 'running')[i]['name']

        #time.sleep(10)

#find_nuke()

text = 'nukeadfgakduhfa'
name1 = re.compile(r'^[mlasu]')
if name1.match(text):
    print text
else:
    print 'none'
    pass

#for i in range(len(qb.jobinfo(status = 'running'))):
#    print qb.jobinfo(status = 'running')[i]

#for i in range(len(qb.hostinfo())):
#    if i == 1:
#        print qb.hostinfo()[1]['workers']

#print qb.jobinfo(id = 34171)
# qb.jobinfo(id = 34171 )[0]['name']
#print qb.jobinfo(id = 34171 )[0]['status']



'''
[Job({'cpustally':
    {'complete': 0, 'badlogin': 0, 'unknown': 0, 'running': 0, 'failed': 0, 'waiting': 0, 'suspended': 0, 'killed': 0, 'pending': 0, 'blocked': 60},
    'cpus': 60, 'preflights': '', 'path': '',
    'flagsstring': 'auto_mount', 'retrysubjob': 2,
    'label': 'qube0', 'pathmap': {}, 'lastupdate': 1449215100,
    'postflights': '', 'retrywork_delay': 15, 'prototype': 'cmdrange', 'mailaddress': '',
    'prod_custom1': 'task', 'prod_custom3': '', 'prod_custom2': '', 'prod_custom5': '',
    'prod_custom4': '', 'account': '', 'agenda_preflights': '', 'agendastatus': 'blocked', 'kind': '',
    'agenda_postflights': '', 'name': 'katana2.1(arnold) (TST) arnold_test_ja(Render)[0,0,3,1-s-c] zhangkh',
    'notes': '', 'agenda_timeout': -1, 'timesubmit': 1449209317, 'hosts': '', 'timeout': -1, 'globalorder': 0,
    'prod_client': '', 'omithosts': '', 'timecomplete': 946702800, 'priority': 998, 'prod_show': 'TST', 'domain': '.',
    'localorder': 0, 'hostorder': '', 'reservations': 'host.processors=1', 'pid': 1, 'timestart': 946702800, 'cluster': '/',
    'todo': 597, 'omitgroups': '', 'requirements': 'host.os=linux', 'pgrp': 34171, 'agendatimeout': -1, 'id': 34171, 'env': {},
    'prod_seq': 'zhangkh', 'flags': 8, 'cwd': '/tmp', 'p_agenda_priority': -1, 'status': 'blocked', 'prod_shot': 'katana',
    'p_agenda_cpus': -1, 'todotally': {'complete': 104, 'badlogin': 0, 'unknown': 0, 'running': 0, 'failed': 0, 'waiting': 0,
                                           'suspended': 0, 'killed': 0, 'pending': 0, 'blocked': 493}, 'reason': 'none', 'retrywork': 2,
    'user': 'zhangkh', 'groups': 'G48,G48S60', 'subjobstatus': 'blocked', 'serverid': 0,
    'data': '(=(cmdline=/sw/ple/studio/tool/gene/applauncher/bin/applauncher katana --v 2.1_arnold --appargs --batch --katana-file /ibrix3/TST/task/zhangkh/katana/render_temps/arnold_test_ja.007/arnold_test_ja.katana --render-node Render -t QB_FRAME_START-QB_FRAME_END --threads3d 0 --tile-render 0,0,3,1 --tile-stitch --tile-cleanup)(range=1001-1597)(rangeChunkSize=1))',
    'restrictions': '', 'package': {'cmdline': '/sw/ple/studio/tool/gene/applauncher/bin/applauncher katana --v 2.1_arnold --appargs --batch --katana-file /ibrix3/TST/task/zhangkh/katana/render_temps/arnold_test_ja.007/arnold_test_ja.katana --render-node Render -t QB_FRAME_START-QB_FRAME_END --threads3d 0 --tile-render 0,0,3,1 --tile-stitch --tile-cleanup', 'range': '1001-1597', 'rangeChunkSize': '1'}, 'queue': '',
    'dependency': 'link-complete-work-34168,link-complete-work-34169,link-complete-work-34170', 'max_cpus': -1, 'drivemap': {}, 'prod_dept': 'lgt'})]
'''

