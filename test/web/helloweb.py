#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-11 14:36:23 
#
# Cteated on: 
# **************************************/


def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return '<h1>Hello, %s !</h1'  % (environ['PATH_INFO'][1:] or 'web')
