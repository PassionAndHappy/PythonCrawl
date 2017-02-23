# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:27:35 2016

@author: WD
"""
#导入库
from baidu_tieba_crawl_v2 import *

mySpider = spider()
mySpider.baseurl = 'http://tieba.baidu.com/f?kw=lol&ie=1utf-8&pn='#定义基础url
mySpider.begin_page = int(raw_input(u'请输入起始页码： '))# 定义爬取起始页码
mySpider.end_page = int(raw_input(u'请输入终止页码： '))# 定义爬取终止页码

mySpider.tieba_spider()#开始百度贴吧爬取