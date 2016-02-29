#!/usr/bin/env python
# -*- coding: utf-8 -*-
#***********************************
#
# author: xiangpeng 
# 
# createtime: 2015-11-18 16:47:37  
#
# ***********************************


import re
import urllib2
import HTMLParser
base = "http://bbs.xm.base-fx.com/forum.php"
path = '/sw/ple/workspace/zengxp/webcrawler/'
star = ''
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
        
def download(url):
    content = urllib2.urlopen(url).read()
    format = '[0-9]*\.jpg';
    res = re.search(format,url);
    print 'downloading:',res.group()
    
    filename = path+res.group()
    f = open(filename,'w+')
    f.write(content)
    f.close() 

print '爬虫'

import urllib

def getImg(html):
    reg = r'src="(.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve('http://bbs.xm.base-fx.com/forum.php/'+imgurl,'/sw/ple/workspace/zengxp/webcrawler/%s.png' % x)
        x+=1
    
html = getHtml('http://bbs.xm.base-fx.com/forum.php')
getImg(html)
             

print 'OK?'
#download('http://bbs.xm.base-fx.com/data/attachment/block/91/91f6eece349e8988649fd2a6269e1d18.jpg')













