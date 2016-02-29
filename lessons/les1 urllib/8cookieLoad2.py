#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex


import urllib
import urllib2
import cookielib

fl = raw_input("Input cookie prefix:")
filename = '%scookie.txt'%fl
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#登录的URL 1
url1 = raw_input("Input url 1:")

#name pwd
name = raw_input("Input login name:")
pwd = raw_input("Input login pwd:")
postdata = urllib.urlencode({
				'name':name,
							'pwd':pwd
									})
loginUrl = url1			#'http://url1111.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是同源的
url2 = raw_input("Input url 2:")
reqUrl = url2 # 'http://url22222.com'
#请求访问网址
result = opener.open(reqUrl)
print result.read()
