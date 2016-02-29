#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015.11.06  15:42:26
#
# Cteated on: 
# **************************************/


print '装饰器1';

def decorator(F):
    def new_F(a, b):
        print 'input:', a, b
        return F(a, b)
    return new_F
    
    
# get square sum    
@decorator
def square_sum(a, b):
    return a**2 + b**2
    

# get suqare diff
@decorator
def square_diff(a, b):
    return a**2 - b**2    

    
print square_sum(3, 4)
print square_diff(4, 3)

print '装饰器2'
# a new warpper layer
def pre_str(pre=''):
    # lod decorator
    def decorator(F):
        def new_F(a, b):
            print pre + ' input', a, b
            return F(a, b)
        return new_F
    return decorator       
    
# get square sum
@pre_str('^_^')
def square_sum(a, b):
    return a**2 + b**2
    
print square_sum(3, 5)  

print '装饰类'

def decor(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aClass(age)
        def display(self):
            self.total_display += 1
            print 'total display:', self.total_display
            self.wrapped.display()
    return newClass
    
@decor
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print 'My age is ', self.age
        
eagle = Bird(5)
for i in range(3):
    eagle.display()        
                          







