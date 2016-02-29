#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ***********************************
# author: xiangpeng zeng
#
# time: 2015-11-17 17:59:29 
#
# ***********************************

print '爬虫'

import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve('http://bbs.xm.base-fx.com/forum.php'+imgurl,'/sw/ple/workspace/zengxp/test/%s.png' % x)
        x+=1
    
html = getHtml('http://bbs.xm.base-fx.com/forum.php')
getImg(html)
print getImg(html)     
