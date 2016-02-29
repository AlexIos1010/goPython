#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib2

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()
