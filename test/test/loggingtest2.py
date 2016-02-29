#!/usr/bin/env python
# -*- coding: utf-8 -*-
#************************************
#
# Author: xiangpeng xiang
#
# Create time: 2015-11-25 10:41:21
#
#************************************

print 'logging test two: '

import logging

logger = logging.getLogger()

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger2')
logger2.setLevel(logging.INFO)

# 用于写入日志文件
fh = logging.FileHandler('/sw/ple/workspace/zengxp/test/test/test.log')

# 用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')





