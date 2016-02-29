#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-11 10:42:57 
#
# **************************************/


print 'class test one'
import json
class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score     
    def __str__(self):
        return 'Student object (name: %s; score: %s)' %(self.name, self.score)          
    def print_score(self):
        print '%s : %s' %(self.__name, self__score)
        
bart = Student1('smiths', 78)
print bart.name
print bart.score
print bart


print 'class test two'

class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score     
     
    def get_name(self):
        return self.__name
        
    def get_score(self):
        return self.__score  
              
    def print_score(self):
        print '%s : %s' %(self.__name, self__score)
        
bart = Student2('jack', 178)
print bart.get_name()
print bart.get_score()

print 'class test three'
class Student3(object):
   
    def set_name(self, name):
        self.__name = name
        
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
     
    def get_name(self):
        return self.__name
        
    def get_score(self):
        return self.__score  
              
    def print_score(self):
        print '%s : %s' %(self.__name, self__score)
stu = Student3()
stu.set_name('Bob')
stu.set_score(12)
print stu.get_name()
print stu.get_score()

stu.set_name('mari')
stu.set_score(11)
print stu.get_name()
print stu.get_score()

print '\n\n'
print 'class 继承与多态'

class Animal(object):
    def __init__(self, name):
        self.name = name
    def run(self):
        print '%s is running...' % self.name

class Dog(Animal):
    def dogrun(self):
        print 'dog dog dog go go go!'
    pass
class Runnable(object):
    def runnable(self):
        print('ranning...')
class Litterdog(Dog, Runnable):
    pass
    
animal = Animal('Animal')
animal.run()
   
dog = Dog('dog')
dog.run()
dog.dogrun()  
print '\n多重继承 litterdog 继承 dog与Runnable  , dog 继承 animal'
litdog = Litterdog('litterdog')
litdog.run()
litdog.dogrun()
litdog.runnable()





















   

