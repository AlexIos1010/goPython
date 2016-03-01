#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
#	print content
	pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
		                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	p1 = re.compile('<div.*?clearfix">.*?<img.*?<div.*?content">(.*?)<!--(.*?)-->.*?class="number">(.*?)</i>',re.S)
	p2 = re.compile('<div.*?clearfix">.*?<img.*?src="(.*?)".*?<div.*?content">(.*?)<!--(.*?)-->.*?class="number">(.*?)</i>',re.S)
#	items = re.findall(pattern,content)
#	items1 = re.findall(p1,content)
	items2 = re.findall(p2,content)
#	print "Total:",len(items)
#	print "Total1:",len(items1)
	print "Total2:",len(items2)
	for item in items2:
		print item[0],item[1],item[2],item[3],item[4]
		raw_input("Next")
#		break
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason

""""
'<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
		                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)


'<div.*?clearfix">.*?<img.*?<div.*?'+
		                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)


<div class="author clearfix">
<span>
<img src="/static/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="匿名用户"/>
</span>
<span>
<h2>匿名用户</h2>
</span>
</div>
<div class="content">
content!!
<!--1456830793-->
</div>
<div class="stats">
<span class="stats-vote"><i class="number">3850</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/115333864" data-share="/article/115333864" id="c-115333864" class="qiushi_comments" target="_blank">
<i class="number">51</i> 评论










'<div.*?clearfix">.*?<img.*?src="(.*?)".*?<div.*?content">(.*?)<!--(.*?)-->.*?class="number">(.*?)</i>',re.S)


<div class="author clearfix">
<a href="/users/28263854" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2826/28263854/medium/20150508202316.jpg" alt="我的狗狗叫小宝"/>
</a>
<a href="/users/28263854" target="_blank" title="我的狗狗叫小宝">
<h2>我的狗狗叫小宝</h2>
</a>
</div>


<div class="content">

content～～
<!--1456829920-->

</div>



<div class="stats">
<span class="stats-vote"><i class="number">3730</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/115333676" data-share="/article/115333676" id="c-115333676" class="qiushi_comments" target="_blank">
<i class="number">48</i> 评论
</a>



</span>
</div>
"""


