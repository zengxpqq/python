#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pprint
import time

import datetime
import traceback
from functools import wraps
import gc

sys.path.append('/sw/ple/studio/lib')
import butility.timeout
sys.path.append('/usr/local/pfx/qube/api/python')
import qb

ISOTIMEFORMAT = '%Y-%m-%d %X'
ERRORLOGPATH = "/sw/ple/studio/etc/log/server/qube_enlarge_resources/setInstances.log"
TESTPATH = r"/sw/ple/studio/etc/log/server/qube_enlarge_resources/"
JOBSTATUS = ['running', 'pending']
HOSTSTATUS = 'active'
PRIORITYRANGE = {'min':10, 'max':500}
INSTANCERANGE = {'min':1, 'max':200, 'criticality':10}
OSLIST = ['winnt', 'linux']
INTERVALTIME = 120
TIMEOUT = 10


def write_runtimeLog(usetime, error, leavingSlots, resultDict, instancesDict):
    file_path = TESTPATH + time.strftime('%Y-%m-%d', time.localtime()) + '.log'
    title = '*********************************************************************' + time.strftime(ISOTIMEFORMAT, time.localtime()) + '*******************************************************************************\n'
    usetime = '\t' + 'usetime : ' + str(usetime) + '\n'
    error = '\t' + 'error : ' + str(error) + '\n'
    slotsLog = '\t' + 'leavingSlots : ' + str(leavingSlots) + '\n'
    slotDictLog = '\t' + 'SlotsDict : ' + str(resultDict) + '\n'
    instancesDict = '\t' + 'change : ' + str(instancesDict) + '\n'
    end = '**************************************************************************************************************************************************************************\n\n'
    message = title + usetime + error + slotsLog + slotDictLog + instancesDict + end
    with open (file_path,"a") as f:
        f.write(str(message))


def format_properties(listTemplate):
    '''
                    return likes ' {'priority': 100, 'toDoFrames': 1, 'host.os': 'linux', 'completedFrames': 0, 'id': 24003} '
                                                                     or ' {'properties': {'host.qube_build': 'rel-6.6-0006-2014/09/09:14:41:22', 'host.proxy_mode': 'interactive', 'host.qube_version': '6.6-2', 'host.architecture': '', 'host.processor_model': '', 'host.cpus': '1', 'host.os': 'winnt', 'host.kernel_version': '6.1', 'host.worker_mode': 'desktop', 'host.qube_class': '', 'host.processor_speed': '3066', 'host.processor_make': 'GenuineIntel'}, 'resources': {'host.swap': '89/8388607', 'host.cores': '0/24', 'host.processors': '0/1', 'host.memory': '3097/49142'}} '
    '''
    templateReturn = dict()
    if listTemplate:
        if isinstance(listTemplate, qb.Job):
            #print listTemplate.get('requirements')
            templateReturn['requirements'] = dict([x.split('=') for x in listTemplate.get('requirements').split(',')])
            templateReturn['system'] = templateReturn.get('requirements').get('host.os')
            templateReturn['priority'] = listTemplate.get('priority')
            templateReturn['toDoFrames'] = listTemplate.get('todo')
            templateReturn['completedFrames'] = listTemplate.get('todotally').get('complete')
            templateReturn['id'] = listTemplate.get('id')
            templateReturn['dependency'] = listTemplate.get('dependency')
            templateReturn['groups'] = listTemplate.get('groups')
            templateReturn['hosts'] = listTemplate.get('hosts')
            templateReturn['omithosts'] = listTemplate.get('omithosts')
            templateReturn['omitgroups'] = listTemplate.get('omitgroups')
            templateReturn['cpus'] = listTemplate.get('cpus')
            templateReturn['max_cpus'] = listTemplate.get('max_cpus')
            templateReturn['user'] = listTemplate.get('user')
        elif isinstance(listTemplate, qb.Host):
            templateReturn['properties'] = dict([x.split('=') for x in listTemplate.get('properties').split(',')])
            templateReturn['resources'] = dict([x.split('=') for x in listTemplate.get('resources').split(',')])
            templateReturn['groups'] = listTemplate.get('groups')

    return templateReturn

def obtain_jobsInfo():
    '''
                    obtain all jobs by status likes running, pending
    '''
    jobsInfos = qb.jobinfo(status=JOBSTATUS)
    return jobsInfos

jobsInfos = obtain_jobsInfo()
#print 'jobsInfos : '
#print jobsInfos

def analysis_jobsInfo(jobsInfos):
    '''
                    structure custom list()
                    return likes [{'priority': 20, 'frames': 353, 'system': 'winnt', 'jobId': 23465, 'groups': 'G48', 'cpus':90, 'max_cpus':-1},]
    '''
    resultList = list()

    for jobsInfo in jobsInfos:
        properties = format_properties(jobsInfo)
        if properties.get('priority') > PRIORITYRANGE.get('min') and properties.get('priority') < PRIORITYRANGE.get('max'):
            resultList.append({'jobId':properties.get('id'), 
                               'system':properties.get('system'), 
                               'priority':properties.get('priority'), 
                               'frames': properties.get('toDoFrames'), 
                               'groups':properties.get('groups'), 
                               'cpus': properties.get('cpus'), 
                               'max_cpus': properties.get('max_cpus'), 
                               'completedFrames': properties.get('completedFrames'),
                               'user': properties.get('user')})

    return resultList
#print 'analysis_jobsInfo : '
#formatJobsInfos = analysis_jobsInfo(jobsInfos)
#print formatJobsInfos

def obtain_slotsCounts():
    '''
       return likes {'winnt': 100, 'linuxG48': 117, 'linux': 145, 'linuxwrk': 0, 'winntG48S60': 100, 'linuxG24': 28}
       返回 系统资源数 如 win有100台 
    '''
    resultDict = {'winnt': 0, 'linux': 0}
    hostInfos = qb.hostinfo(state=HOSTSTATUS)

    for singleHost in hostInfos:
        properties = format_properties(singleHost)
        resultDict[properties.get('properties').get('host.os')] = resultDict.get(properties.get('properties').get('host.os')) + int(properties.get('resources').get('host.processors').split('/')[1])

        if properties.get('groups'):
            groupKey = properties.get('properties').get('host.os') + properties.get('groups')
            if resultDict.get( groupKey ):
                resultDict[groupKey] = resultDict.get(groupKey) + int(properties.get('resources').get('host.processors').split('/')[1])
            else:
                resultDict[groupKey] = int(properties.get('resources').get('host.processors').split('/')[1])

    return resultDict

#print '\nobtain_slotsCounts:  '
#slotsDict = obtain_slotsCounts()
#print slotsDict

def obtain_outOfScopeCounts():     # there is a problem
    '''
                    gets the count is no within the scope of PRIORITYRANGE
                    return likes '{'winnt': 0, 'linux': 1}'
                     win  linux  
    '''
    resultDict = {'winnt': 0, 'linux': 0}

    hostInfos = qb.hostinfo(state=HOSTSTATUS)

    for singleHost in hostInfos:
        properties = format_properties(singleHost)
        resultDict[properties.get('properties').get('host.os')] = resultDict.get(properties.get('properties').get('host.os')) + int(properties.get('resources').get('host.processors').split('/')[0])
        if properties.get('groups'):
            groupKey = properties.get('properties').get('host.os') + properties.get('groups')
            if resultDict.get( groupKey ):
                resultDict[groupKey] = resultDict.get(groupKey) + int(properties.get('resources').get('host.processors').split('/')[0])
            else:
                resultDict[groupKey] = int(properties.get('resources').get('host.processors').split('/')[0])

    return resultDict

#print 'obtain_outOfScopeCounts :  '
#outOfScopeCounts = obtain_outOfScopeCounts()
#print outOfScopeCounts

def calculate_leavingSlots(slotsDict, outOfScopeCounts):
    '''
       return likes {'winnt': 99, 'winntG48_swap60': 98, 
                     'linuxG48': 30, 'winntG48': 1, 'linuxwrk': 10, 'linux': 244, 'linuxG48_swap60': 2, 'linuxG24': 202}
       
    '''
    leavingSlots = {}
    for system in outOfScopeCounts.keys():
        leavingSlots[system] = slotsDict.get(system) - outOfScopeCounts.get(system)

    return leavingSlots

#print 'calculate_leavingSlots'
#leavingSlots = calculate_leavingSlots(slotsDict, outOfScopeCounts)
#print leavingSlots


def exec_prioritySum(resultList):
    # OSLIST = ['winnt', 'linux']
    for system in OSLIST:
        count = 0
        prioritySum = system + 'PrioritySum'

        for priorityKey in resultList.get(system + 'Total').keys():
            count += priorityKey
        resultList[prioritySum] = count

    return resultList



def exec_statsCounts(formatJobsInfos):
    '''
       return likes {'winntTotal': {},
                     'linuxTotal': {40: {'counts': 1, 'totalFrames': 85},    
                                    100: {'counts': 5, 'totalFrames': 5}},
                     'linuxPrioritySum': 140,       
                     'winntPrioritySum': 0}
                     {'winntTotal': {150: {'counts': 1, 'totalFrames': 115, 'completed': 6, 'imcompleted': 109}}, 
                      'linuxTotal': {40: {'counts': 2, 'totalFrames': 253, 'completed': 16, 'imcompleted': 237},
                                     100: {'counts': 1, 'totalFrames': 80, 'completed': 12, 'imcompleted': 68},
                                     150: {'counts': 8, 'totalFrames': 482, 'completed': 0, 'imcompleted': 482}}, 
                      'winntPrioritySum': 150, 
                      'linuxPrioritySum': 290}
        
    '''
    resultList = {'linuxTotal':{}, 'winntTotal':{}, 'linuxPrioritySum':0, 'winntPrioritySum':0}

    for singleJob in formatJobsInfos: 
        total = resultList.get((singleJob.get('system') + 'Total').strip())
        
        if total.get(singleJob.get('priority')):

            total.get(singleJob.get('priority'))['completed'] = total.get(singleJob.get('priority')).get('completed') + singleJob.get('completedFrames')

            total.get(singleJob.get('priority'))['totalFrames'] = total.get(singleJob.get('priority')).get('totalFrames') + singleJob.get('frames')
            
            total.get(singleJob.get('priority'))['imcompleted'] =  total.get(singleJob.get('priority')).get('imcompleted') + singleJob.get('frames') - singleJob.get('completedFrames')
            total.get(singleJob.get('priority'))['counts'] = total.get(singleJob.get('priority')).get('counts') + 1
            
            total.get(singleJob.get('priority'))['groups'] = singleJob.get('groups')
        else:
            #total[singleJob.get('priority')] = {'totalFrames':singleJob.get('frames'), 'counts':1}
            total[singleJob.get('priority')] = {'totalFrames':singleJob.get('frames'),
                                                'counts':1,
                                                'completed': singleJob.get('completedFrames'),
                                                'imcompleted': singleJob.get('frames') - singleJob.get('completedFrames'),
                                                'groups': singleJob.get('groups')}

    resultList = exec_prioritySum(resultList)

    return resultList
#print '\n exec_statsCounts : '
#statsCounts = exec_statsCounts(formatJobsInfos)
#print statsCounts


def exec_needlessSlots(statsCounts):
    for system in OSLIST:
        needLessCounts = 0
        total = statsCounts.get(system + 'Total')
        rangeIndex = len(total.keys()) - 1

        for priorityKey in reversed(total.keys()):
            # 判断 当前优先级 未完成 的总帧数是否小于 slots
            if total.get(priorityKey).get('imcompleted') < total.get(priorityKey).get('slots'):
                # 
                needLessCounts = needLessCounts + ( total.get(priorityKey).get('slots') - total.get(priorityKey).get('imcompleted') )
                total.get(priorityKey)['slots'] = total.get(priorityKey).get('imcompleted')

        while rangeIndex >= 0:
            priority = total.keys()[rangeIndex]
            if total.get( priority ).get('imcompleted') > total.get( priority ).get('slots'):
                if needLessCounts > ( total.get( priority ).get('imcompleted') - total.get( priority ).get('slots')):
                    total.get( priority )['slots'] = total.get( priority ).get('imcompleted')
                    needLessCounts = needLessCounts - ( total.get( priority ).get('imcompleted') - total.get( priority ).get('slots'))
                else:
                    total.get( priority )['slots'] = total.get( priority ).get('slots') + needLessCounts
                    needLessCounts = 0
                    break
            rangeIndex -= 1

    return statsCounts
# leavingSlots = calculate_leavingSlots(slotsDict, outOfScopeCounts)
# statsCounts = exec_statsCounts(formatJobsInfos)
def exec_calculateSlots(leavingSlots, statsCounts):
    '''
                    {'winntTotal': {150: {'slots': 0, 'counts': 1, 'totalFrames': 115, 'completed': 6, 'imcompleted': 109}}, 
                     'linuxTotal': {40: {'slots': 0, 'counts': 1, 'totalFrames': 178, 'completed': 104, 'imcompleted': 74}, 
                                    150: {'slots': 0, 'counts': 3, 'totalFrames': 161, 'completed': 0, 'imcompleted': 161}}, 
                     'winntPrioritySum': 150, 
                     'linuxPrioritySum': 190}

    '''
    for system in OSLIST:
        total = statsCounts.get(system + 'Total')
        prioritySum = statsCounts.get(system + 'PrioritySum')
        
        rangeIndex = len(total.keys()) - 1
        totalleaving = 0
        for priorityKey in sorted(total.keys()):
            if total.get(priorityKey)['groups']:
                listgroups = total.get(priorityKey)['groups'].split(',')
                for i in listgroups:
                    if leavingSlots.get(system + i) == None:
                        continue
                    else:
                        totalleaving = totalleaving + leavingSlots.get(system + i)
                total.get(priorityKey)['slots'] =  int( ( float(total.keys()[rangeIndex]) / prioritySum ) * totalleaving )
            else:
                total.get(priorityKey)['slots'] =  int( ( float(total.keys()[rangeIndex]) / prioritySum ) * leavingSlots.get(system) )    #Algorithm
            rangeIndex -= 1
    statsCounts = exec_needlessSlots(statsCounts)
    

    return statsCounts

#print 'exec_calculateSlots'
#calculatedSlots =  exec_calculateSlots(leavingSlots, statsCounts)
#print calculatedSlots

def exec_compareInstances(singleJob, instances):
    if singleJob.get('max_cpus') != -1:
        if instances > singleJob.get('max_cpus'):
            singleJob['instances'] = singleJob.get('max_cpus')
        else:
            singleJob['instances'] = instances
    else:
        if singleJob.get('frames') <= INSTANCERANGE.get('criticality'):
            singleJob['instances'] = singleJob.get('frames') - singleJob.get('completedFrames')
        elif instances > singleJob.get('frames'):
            singleJob['instances'] = singleJob.get('frames') - singleJob.get('completedFrames')
        elif instances < INSTANCERANGE.get('min'):
            singleJob['instances'] =  singleJob.get('cpus')
        elif instances + singleJob.get('cpus') < singleJob.get('frames'):
            if singleJob.get('cpus') + instances > singleJob.get('frames') - singleJob.get('completedFrames'):
                singleJob['instances'] = singleJob.get('frames') - singleJob.get('completedFrames')
            else:
                singleJob['instances'] = instances + singleJob.get('cpus')
        elif instances + singleJob.get('cpus') > singleJob.get('frames'):
            singleJob['instances'] = singleJob.get('frames') - singleJob.get('completedFrames')              
        else:
            singleJob['instances'] = instances

    return singleJob

# formatJobsInfos = analysis_jobsInfo(jobsInfos)
# calculatedSlots = exec_calculateSlots(leavingSlots, statsCounts)
def exec_calculateInstances(calculatedSlots, formatJobsInfos):
    '''
       return likes [{'priority': 20, 'frames': 80, 'instances': 80, 'system': 'winnt', 'jobId': 23624}, ]
    '''
    instancesDict = {}
    for singleJob in formatJobsInfos:
        total = calculatedSlots.get((singleJob.get('system') + 'Total').strip())
        #  uncompleted of shots  /  uncompleted of priority   *   当前优先级分配的资源
        if total.get(singleJob.get('priority')).get('imcompleted') == 0:
            instance = 0
        else:
            instances = int( (float(singleJob.get('frames') - singleJob.get('completedFrames') ) /
                              total.get(singleJob.get('priority')).get('imcompleted')) *
                              total.get(singleJob.get('priority')).get('slots') )

        singleJob = exec_compareInstances(singleJob, instances)

        instancesDict[singleJob['jobId']] = singleJob

    return instancesDict

#print '\n exec_calculateInstances : '
#instancesDict = exec_calculateInstances(calculatedSlots, formatJobsInfos)
#print instancesDict

def exec_instancesDict(instancesDict, slotsDict):
    contentlist = []
    for single in instancesDict:
        init_cpus = instancesDict[single].get('cpus')
        instance = instancesDict[single].get('instances')
        content = ''
        if instance > init_cpus and instance <= slotsDict[(instancesDict[single].get('system')).strip()]:
            start = '****************   '
            jobid = 'jobid : ' + str(single) 
            user =  '     user  : ' + instancesDict[single].get('user') 
            
            frames = '     frames : ' + str(instancesDict[single].get('frames')) 
            
            cpus = '     init_instance : ' + str(init_cpus)
                  
            instance =  '    change instances : ' + str(instancesDict[instancesDict[single].get('jobId')].get('instances'))
             
            #qb.modify({'cpus': instancesDict[single].get('instances')}, instancesDict[single].get('jobId'))
            end = '    *****************************     '
            content = start + jobid + user + frames + cpus + instance + end
            contentlist.append(content)
    return contentlist

def modify_jobInstances(instancesDict, slotsDict):
    for single in instancesDict:
        init_cpus = instancesDict[single].get('cpus')
        instance = instancesDict[single].get('instances')
        #print slotsDict[instancesDict[single].get('system')]
        if instance > init_cpus and instance <= slotsDict[(instancesDict[single].get('system')).strip()]:
            print '**************************************'
            print 'jobid : ' + str(single)
            print 'user  : ' + instancesDict[single].get('user')
            
            print 'frames : ' + str(instancesDict[single].get('frames'))
            
            print 'init_instance : ' + str(init_cpus)
                  
            print 'change instances : ' + str(instancesDict[instancesDict[single].get('jobId')].get('instances'))
            qb.modify({'cpus': instancesDict[single].get('instances')}, instancesDict[single].get('jobId'))   
                
            print '***************************************\n'


def exec_calculate():
    print '[%s]' % time.strftime('%Y-%m-%d %H:%M:%S'), 'server started.'

    #while True:
    error = ''
    content = []
    calculatedSlots = {}
    try:
        start_time = datetime.datetime.now()
        #Initialization   
        # get the jobs (state = running | pending ) information
        jobsInfos = obtain_jobsInfo()
        
        # {'winnt': 50, 'linuxG48': 117, 'winntG48S60': 50, 'linuxG48S60': 50, 'linuxwrk': 0, 'linux': 195, 'linuxG24': 28}
        slotsDict = obtain_slotsCounts()

        #Get Available Slots
        outOfScopeCounts = obtain_outOfScopeCounts()
        leavingSlots = calculate_leavingSlots(slotsDict, outOfScopeCounts)

        #Calculate By Algorithm
        # filter the jobInfos by  10 < priority < 200
        formatJobsInfos = analysis_jobsInfo(jobsInfos)
        statsCounts = exec_statsCounts(formatJobsInfos)
        
        calculatedSlots =  exec_calculateSlots(leavingSlots, statsCounts)

        instancesDict = exec_calculateInstances(calculatedSlots, formatJobsInfos)
        content = exec_instancesDict(instancesDict, slotsDict)
        
        
        modify_jobInstances( instancesDict, slotsDict)
    except:
        error = traceback.format_exc()
        
    end_time = datetime.datetime.now()
    usetime = end_time - start_time    
    write_runtimeLog(usetime, error, leavingSlots, calculatedSlots, content)
        
    #time.sleep(INTERVALTIME)
    gc.collect()
        
        

def main():
    exec_calculate() 
        

if __name__ == '__main__':
    main()



