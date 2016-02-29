#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-12 15:47:50 
#
# Cteated on: 
# **************************************/


print '常用内建模块'
# namedtuple 是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。 
print 'collections -> namedtuple'

from collections import namedtuple
# namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y
print p

print isinstance(p, Point)
print isinstance(p, tuple)

print '\ndeque是为了高效实现插入和删除操作的双向列表，适用于队列和栈'
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

print '\ndefaultdict: key不存在时，返回一个默认值'
from collections import defaultdict
dic = defaultdict(lambda: 'N/A')
dic['a'] = 'zxc'
print dic['a']
print dic['c']

print '\n OrderedDict: 保持Key的顺序'
#from collections import OrderedDict
#d = dic([('a', 1), ('b', 2), ('c', 3)])
#print d

#from collections import Counter


