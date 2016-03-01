#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib
import urllib2
import re 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
  
page = raw_input("Page:")
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
#print url
try:
	request = urllib2.Request(url,headers=headers)
	response = urllib2.urlopen(request)
#	print "\nScource:",response.read()
	content = response.read().decode('utf-8')
	pattern = re.compile('<div.*?class="content">(.*?)<!--(.*?)-->.*?</div>',re.S)
	items = re.findall(pattern,content)
	mode = raw_input ("Parse finised\nS for save,other for display")
	for item in items:
		if mode == "S":
			jokes = '\n'.join(item)
			f = open("hot%s"%page,"ab")
			f.write(jokes)
			f.close()
			print "Saved"
		else:
			print item[0]
			raw_input("Next")

except urllib2.URLError, e:
	if hasattr(e,"code"):
		print "\nExp Code:",e.code
	if hasattr(e,"reason"):
		print "\nExp reason:",e.reason
	
#<div class="content">(.*?)<!--(.*?)-->.*?</div>


