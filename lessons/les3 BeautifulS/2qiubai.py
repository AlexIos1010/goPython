#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib
import urllib2

from bs4 import BeautifulSoup

page = raw_input("Page:")
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)  Chrome/47.0.2526.73 Safari/537.36"
headers={'User-Agent':user_agent} 
#html_doc = """ """
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html_doc = response.read().decode('utf-8')
#    print html_doc
    soup = BeautifulSoup(html_doc)
#    print soup.title
#    print soup.find_all(class="content")
    print soup.get_text()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print "\nExp Code:",e.code
    if hasattr(e,"reason"):
        print "\nExp reason:",e.reason


"""
soup = BeautifulSoup(html_doc)

print soup.title

print soup.title.name

print soup.title.string

print soup.find_all('a')

print soup.find(id='link3')

print soup.get_text()
"""
