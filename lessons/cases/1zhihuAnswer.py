#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib
import urllib2
import re 
  
page = 30237432#raw_input("Number:")
url = 'http://www.zhihu.com/question/' + str(page)
#print url
try:
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
#	print "\nScource:",response.read()
	content = response.read().decode('utf-8')
	pattern = re.compile('<div class="zh-summary summary clearfix" style="display:none;">(.*?)</div>',re.S)
	items = re.findall(pattern,content)
	titleP = re.compile('<title>(.*?)</title>',re.S)
	cp1 = re.compile('<div class="zm-editable-content">(.*?)</div>',re.S)
	cp2 = re.compile('<div class="zh-summary summary clearfix" style="display:none;">(.*?)</div>',re.S)
	cp3 = re.compile('<div class="zm-editable-content clearfix">(.*?)</div>',re.S)
	cp4 = re.compile('<div.*?>(.*)</div>',re.S)
	title = re.findall(titleP,content)
	c1 = re.findall(cp1,content)
	c2 = re.findall(cp2,content)
	c3 = re.findall(cp3,content)
	c4 = re.findall(cp4,content)
	print len(c4)
	raw_input("Start")
	print "title len:",len(title)
	print "c1-4 len:",len(c1),len(c2),len(c3),len(c4)
	for c11 in c1:
		print "c11:",c11
		raw_input('Next')
	for c22 in c2:
		print "c22:",c22
		raw_input('Next')
	for c33 in c3:
		print c33
		raw_input('Next')
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print "\nExp Code:",e.code
	if hasattr(e,"reason"):
		print "\nExp reason:",e.reason

#<title>(.*?)</title>
#<div class="zm-editable-content">(.*?)</div>
#<div class="zh-summary summary clearfix" style="display:none;">(.*?)</div>
#<div class="zm-editable-content clearfix">(.*?)</div>


