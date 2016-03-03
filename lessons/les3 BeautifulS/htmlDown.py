#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib2

url = raw_input('Input Website:')
user_agent = ''
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    content_encode = content.encode('utf-8')
    print 'get web:',len(content)
    html_f = open('1.html','wb')
    html_f.write(content_encode)
    html_f.close()
    print 'Saved'
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print "\nExp Code:",e.code
    if hasattr(e,"reason"):
        print "\nExp reason:",e.reason
