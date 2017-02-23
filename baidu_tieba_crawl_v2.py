# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:27:35 2016

@author: WD
"""
# 百度贴吧html_content获取

#导入库
import urllib2
import time


class spider():
    def __init__(self):
        self.isSuccess = False
        self.baseurl = None
        self.url = None
        self.beginPage = None
        self.endPage = None
        self.user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'#建立伪装身份
        self.headers = {'User-Agent':self.user_agent}         #建立伪装字典
        self.req = None
        self.response = None
        self.html_content = None
        self.file_name = None
        self.timeout = 0.5
        
    
    def setisSuccess(self, status):
        self.isSuccess = status
        
    def getisSuccess(self):
        return self.isSuccess
        

    #===========定义获取html_content函数==============
    def Crawl(self):# 专用于返回html_content
        try:
            self.req = urllib2.Request(self.url, headers = self.headers)#新建请求
            try:
                self.response = urllib2.urlopen(self.req)      #请求服务器
                try:
                    self.html_content = self.response.read()   #获取响应内容
                    self.setisSuccess(True)
                except:
                    print u'获取响应内容失败...'
                    self.isSuccess = False
            except:
                print '请求服务器失败！'   
        except:
            self.html_content = None
            
        return self.html_content     #返回html_content内容
    
        #========定义文件写入函数===============
    def write_to_html(self):
        try:
            f = open(self.file_name,'w+')# 打开文件
            try:
                f.write(self.html_content)  #写入内容
            except IOError, e:
                print '写入文件失败...',e
        except IOError, e:
             print '文件打开失败...',e
        finally:
            f.close()               #关闭文件   
    
    
    #===========定义url组装函数===========
    def tieba_spider(self):
        for i in range(self.begin_page, self.end_page+1):
            pn = 50 * (i-1)
            self.url = self.baseurl + str(pn)
            print u'正在下载第' + str(i) + u'页的内容...'
            self.html_content = self.Crawl()
            if self.getisSuccess() == True:
                print 'Crawl The Page ' ,i,' successful!'
            else:
                print 'Crawl The Page ' + str(i) +' failed!'

            self.file_name = str(i) + '.html'
            self.write_to_html()
            time.sleep(self.timeout)
            
            
 

#===========定义main方法==============
if __name__ == '__main__': 
    mySpider = spider()
    mySpider.baseurl = 'http://tieba.baidu.com/f?kw=lol&ie=1utf-8&pn='#定义基础url
    mySpider.begin_page = int(raw_input(u'请输入起始页码： '))# 定义爬取起始页码
    mySpider.end_page = int(raw_input(u'请输入终止页码： '))# 定义爬取终止页码
    
    mySpider.tieba_spider()#开始百度贴吧爬取








