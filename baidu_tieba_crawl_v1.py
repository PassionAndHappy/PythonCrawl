# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:27:35 2016

@author: WD
"""
# 百度贴吧HTML获取

#导入库
import urllib2

#========定义文件写入函数===============
def write_file(file_name,txt):
    f = open(file_name,'w+')# 打开文件
    f.write(txt)            #写入内容
    f.close()               #关闭文件

#===========定义获取html函数==============
def Crawl(url):# 专用于返回html
    user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'#建立伪装身份
    headers = {'User-Agent':user_agent}         #建立伪装字典
    req = urllib2.Request(url,headers = headers)#新建请求
    response = urllib2.urlopen(req)             #请求服务器
    html = response.read()                      #获取响应内容
    return html                                 # 返回HTML内容

#===========定义url组装函数===========
def tieba_spider(baseurl,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        pn = 50*(i-1)
        url = baseurl + str(pn)
        html = Crawl(url)
        file_name = str(i) + '.html'
        print '正在下载第' + str(i) + '页的内容'
        write_file(file_name,html)
        
    
    

#===========定义main方法==============
if __name__ == '__main__':
    baseurl ='http://tieba.baidu.com/f?kw=lol&ie=1utf-8&pn='#定义基础url
    begin_page = int(raw_input(u'请输入起始页码： '))# 定义爬取起始页码
    end_page = int(raw_input(u'请输入终止页码： '))# 定义爬取终止页码
    
    tieba_spider(baseurl, begin_page, end_page)#开始百度贴吧爬取







