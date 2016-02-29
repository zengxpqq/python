#!/bin/env python
# -*- coding: utf-8 -*-
# /**************************************
#
# Author: xiangpeng zeng
# Created on: 2015-11-11 14:36:23 
#
# ***************************************
import os

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

