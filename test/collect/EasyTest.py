#!/usr/bin/env python
import sys
import bcommunication.base_message as baseMessage
import bcommunication.base_email as baseEmail
import time
def qubeMonitor(result):
    '''
    Arguments:
        monitorType: string likes "jobs" or "workers"
        id: Job or Worker id
        state: current state
        changedTime: status changed time
        
        recipients: can be a a list of users, likes ['chenrong', '']
        content: message content
        title: email's title 
    '''
    
    recipients = ['chenrong', ]
    title = '[QubeMonitor]'
    id = str(result['id'])
    status = result['status']
    changedTime = result['changedTime']
    opeart = result['opeart']
    
    content = id + ' ' + status + ' ' + changedTime
    
    if opeart == 'mes':
        baseMessage.send(recipients, content)
    elif opeart == 'email':
        baseEmail.send(recipients, title, content)
    elif opeart == 'log':
        clean_result=list()
	for sub_result in result:
	    if sub_result not in clean_result:
		clean_result.append(sub_result)
	file_time  = time.strftime('%Y-%m-%d')
	file_name = file_time +".log"
	path = r"/sw/ple/workspace/tianfd/qube_wrangler_callback/conf/"
	file_path = path+file_name  
	print file_path
	new = open(file_path,"a")
	new.close()
	with open (file_path,"a") as f:
	    for i in range(len(clean_result)):
		f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
		f.write("\n")
		f.write(str(clean_result[i]))
		f.write("\n")
    else:
	raise "no such method!"

#def write_log(result):
#    clean_result=list()
#    for sub_result in result:
#        if sub_result not in clean_result:
#            clean_result.append(sub_result)
#    file_time  = time.strftime('%Y-%m-%d')
#    file_name = file_time +".log"
#    path = r"/sw/ple/workspace/tianfd/qube_wrangler_callback/conf/"
#    file_path = path+file_name  
#    print file_path
#    new = open(file_path,"a")
#    new.close()
#    print len(clean_result)
#    print clean_result
#    with open (file_path,"a") as f:
#        for i in range(len(clean_result)):
#            f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
#            f.write("\n")
#            f.write(str(clean_result[i]))
#            f.write("\n")
"""
def write_log(result):
    file_time  = time.strftime('%Y-%m-%d')
    file_name = file_time +".log"
    path = r"/sw/ple/workspace/tianfd/qube_wrangler_callback/conf/"
    file_path = path+file_name  
    print file_path
    new = open(file_path,"a")
    new.close()
    with open (file_path,"a") as f:
        f.write(str(result))
   """    

def call_back(search_list):
	for items in search_list:
		qubeMonitor({'status': 'running', 'changedTime': '2015-08-03 15:40:17', 'id': 17097, 'opeart': 'log'})