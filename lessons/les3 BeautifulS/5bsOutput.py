#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#格式化输出
#prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,
#每个XML/HTML标签都独占一行
soup = BeautifulSoup(html_doc)
'''
print (soup.prettify())
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
'''

'''
print '#type(soup.a):',type(soup.a)
print "#type(soup.find_all('a')):",type(soup.find_all('a'))
print "#type(soup.a.prettify()):",type(soup.a.prettify())
#type(soup.a): <class 'bs4.element.Tag'>
#type(soup.find_all('a')): <class 'bs4.element.ResultSet'>
#type(soup.a.prettify()): <type 'unicode'>
'''

#压缩输出
#如果只想得到结果字符串,不重视格式,那么可以对一个 BeautifulSoup 对象或 Tag 对象使用Python的 unicode() 或 str() 方法:
'''
print '#',str(soup.a)
print '#',unicode(soup.a)
print '#prettify',soup.a.prettify()
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#prettify <a class="sister" href="http://example.com/elsie" id="link1">
# Elsie
#</a>
'''

#输出格式
#Beautiful Soup输出是会将HTML中的特殊字符转换成Unicode,比如“&lquot;”:
'''
soupSpecial = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.")
print '#',unicode(soupSpecial)
# Traceback (most recent call last):
  File "bsOutput.py", line 90, in <module>
    print '#',unicode(soupSpecial)
UnicodeEncodeError: 'ascii' codec can't encode character u'\u201c' in position 15: ordinal not in range(128)

#print '#',str(soupSpecial)
# <html><body><p>“Dammit!” he said.</p></body></html>
'''


