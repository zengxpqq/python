#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

enlargepath = os.getcwd()

while True:
    if time.localtime().tm_hour < 23 and time.localtime().tm_hour > 7:
        #if time.localtime().tm_min < 30:
            os.system('python ' + enlargepath + '/enlargetwo.py')
    time.sleep(120)
