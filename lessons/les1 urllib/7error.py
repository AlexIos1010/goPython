#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib2
 
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
	urllib2.urlopen(req)
except urllib2.HTTPError, e:
	print e.code
except urllib2.URLError, e:
	print e.reason
else:
	print "OK"


#or
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
	urllib2.urlopen(req)
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
else:
	print "OK"

