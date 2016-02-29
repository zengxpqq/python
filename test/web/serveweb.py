#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-11 14:36:23 
#
# Cteated on: 
# **************************************/

# 从wsgire模块导入
from wsgiref.simple_server import make_server

# 导入自己编写的application函数
from helloweb import application

# 创建一个服务器，ip地址为空，端口号是8080，处理函数是application
httpd = make_server('', 8080, application)
print 'Serving HTTP on port 8080...'

# 开始监听HTTP请求
httpd.serve_forever()
