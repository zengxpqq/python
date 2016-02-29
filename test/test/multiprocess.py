#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-12 09:09:13  
#
# **************************************/

from multiprocessing import Process, Pool
import os, time, random

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' %(name, os.getpid())
    
if __name__ == '__main__':
    print 'Parent Process %s. ' % os.getpid()
    p = Process(target = run_proc, args = ('test', ))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'    
    
print '\n进程池'

def long_time_task(name):
    print 'Run task %s (%s)...' %(name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' %(name, (end - start))
    
if __name__ == '__main__':        #表示程序作为主程序执行，而不是使用import作为模块导入
    print 'Parents process %s.' %os.getpid()
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task, args = (i, ))
    print 'Waiting for all subprocesses done...'
    p.close() # 调用close()之后就不能继续添加新的Process了。
    p.join()  # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()。
    print 'All subprocesses done.'   
    
    
print '\n多线程'

import threading
# 新线程执行代码：
def loop():
    print 'thread %s is running...' %threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s ' %(threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' %threading.current_thread().name
    
print 'thread %s is running...' %threading.current_thread().name
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print 'thread %s ended.' %threading.current_thread().name  

print '\n创建全局ThreadLocal对象:'
local_school = threading.local()   # 可以把local_school看成全局变量

def process_student():
    print 'Hello, %s (in %s)' %(local_school.student, threading.current_thread().name)
    
def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student = name     # 每个属性如local_school.student 都是线程的局部变量，互补干扰
    process_student()
    
t1 = threading.Thread(target = process_thread, args = ('Alice', ), name = 'A')
t2 = threading.Thread(target = process_thread, args = ('Bob', ), name = 'B')
t1.start()
t2.start()
t1.join()
t2.join()        
      
 
