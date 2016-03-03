#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib2

from bs4 import BeautifulSoup

url = 'http://stackoverflow.com/questions'
user_agent = ''
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html_doc = response.read().decode('utf-8')
    html_encode = html_doc.encode("utf-8")
#    print html_doc
    fname = raw_input('Input file name')
    fhtml = open('%s.html'%fname, "wb")
    fhtml.write(html_encode)
    fhtml.close()
    print '%s Saved'%fname
    soup = BeautifulSoup(html_doc)
#    print soup.find(id='questions')
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print "\nExp Code:",e.code
    if hasattr(e,"reason"):
        print "\nExp reason:",e.reason


