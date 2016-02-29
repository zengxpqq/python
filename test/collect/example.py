#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
sys.path.append('/job/BFX/gene/lib/python/pexpect-2.3')
import pexpect
import socket
from optparse import OptionParser

sys.path.append("/job/BFX/gene/base_pipeline/qube")
import currentJob

#get qb path and import qb module
if os.environ.has_key('QUBE_LOCATION'):
    qb_path = os.environ['QUBE_LOCATION']
else:
    qb_path = '/usr/local/pfx/qube'

if qb_path:
    qb_api = qb_path+'/api/python'
else:
    qb_api = '/usr/local/pfx/qube/api/python'
sys.path.append(qb_api)
import qb

#get current host info
name=socket.gethostname()
if name!="qube.xm.base-fx.com":
    try:
        hostinfo = qb.hostinfo(name=name)[0]
        props = dict([x.split('=') for x in hostinfo['properties'].split(',')])
        cpus = int(props['host.cpus'])
        if hostinfo['locks']:
            locks = dict([x.split('=') for x in hostinfo['locks'].split(',')])
        else:
            locks=None
    except:
        print '%s,This Machine Has Been Removed From Qube Render Farm.....'%name
        locks=None
else:
    locks=None

def lock(option,name=''):
    cmd = '''su qube -c "qblock %s %s"'''%(option,name)
    #print cmd

    child = pexpect.spawn(cmd)
    i = child.expect([pexpect.TIMEOUT,'Password:','???'])
    #print i
    if i == 0:
        print 'cant connect to supeuser'
        sys.exit()
    elif i==1 or 2:
        child.sendline('bfx70cd')
        child.expect(pexpect.EOF)


def autoOpt():
    #print locks
    if locks:
        if locks.has_key('host.processor_all'):
            if locks['host.processor_all']=='0' or locks['host.processor_all']!='1':
                return '--purge'
            else:
                return '--unlock'
        else:
            return '--unlock'
    else:
        return '--all --purge'
if __name__ == '__main__':
    appname = sys.argv[0]
    usage = '%s [OPTION] arg'%appname
    parser = OptionParser(usage=usage)
    parser.add_option('-l', '--lock', action='store_true', help='lock all processors of the current host')
    parser.add_option('-u', '--unlock', action='store_true', help='unlock all processors of the current host')
    parser.add_option('-f', '--file',  help='assign the lock in the file to all processors of the current host')

    (options,args)=parser.parse_args()

    #print options
    lockall = '--purge'
    unlock = '--unlock'
    file = None
    
    try:
        testhostinfo = qb.hostinfo(name=name)[0]
        if options.lock==options.unlock==options.file==None:
            option = autoOpt()
            lock(option,name)
            if option==lockall:
                print "All processers on worker '%s' are locked"%name
            elif option==unlock:
                print "All processers on worker '%s' are unlocked"%name
        elif options.lock:
            lock(lockall,name)
            print "All processers on worker '%s' are locked"%name
            job = currentJob.currentJob()
            job.killJob()
        elif options.unlock:
            lock(unlock,name)
            print "All processers on worker '%s' are unlocked"%name
        elif options.file:
            if os.path.isfile(options.file):
                file = "--group user --all --file %s"%options.file
                lock(file)
                print "All workers in user group are scheduled"
    except:
        print '%s,This Machine Has Been Removed From Qube Render Farm....'%name
        