#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

from bs4 import BeautifulSoup


#指定文档解析器
'''
如果仅是想要解析HTML文档,只要用文档创建 BeautifulSoup 对象就可以了.Beautiful Soup会自动选择一个解析器来解析文档.但是还可以通过参数指定使用那种解析器来解析当前文档.

BeautifulSoup 第一个参数应该是要被解析的文档字符串或是文件句柄,第二个参数用来标识怎样解析文档.如果第二个参数为空,那么Beautiful Soup根据当前系统安装的库自动选择解析器,解析器的优先数序: lxml, html5lib, Python标准库.在下面两种条件下解析器优先顺序会变化:

    要解析的文档是什么类型: 目前支持, “html”, “xml”, 和 “html5”
    指定使用哪种解析器: 目前支持, “lxml”, “html5lib”, 和 “html.parser”
    安装解析器 章节介绍了可以使用哪种解析器,以及如何安装.

    如果指定的解析器没有安装,Beautiful Soup会自动选择其它方案.目前只有 lxml 解析器支持XML文档的解析,在没有安装lxml库的情况下,创建 beautifulsoup 对象时无论是否指定使用lxml,都无法得到解析后的对象
'''

#解析器之间的区别
#Beautiful Soup为不同的解析器提供了相同的接口,但解析器本身时有区别的.同一篇文档被不同的解析器解析后可能会生成不同结构的树型文档.区别最大的是HTML解析器和XML解析器,看下面片段被解析成HTML结构:
'''
print '#BeautifulSoup("<a><b /></a>"):',BeautifulSoup("<a><b /></a>")
#BeautifulSoup("<a><b /></a>"): <html><body><a><b></b></a></body></html>

#因为空标签<b />不符合HTML标准,所以解析器把它解析成<b></b>
'''

#同样的文档使用XML解析如下(解析XML需要安装lxml库).注意,空标签<b />依然被保留,并且文档前添加了XML头,而不是被包含在<html>标签内:
'''
print '#:BeautifulSoup("<a><b /></a>:\n", "xml")',BeautifulSoup("<a><b /></a>", "xml")
#:BeautifulSoup("<a><b /></a>:
", "xml") <?xml version="1.0" encoding="utf-8"?>
<a><b/></a>
'''


##HTML解析器之间也有区别,如果被解析的HTML文档是标准格式,那么解析器之间没有任何差别,只是解析速度不同,结果都会返回正确的文档树.

#但是如果被解析文档不是标准格式,那么不同的解析器返回结果可能不同.下面例子中,使用lxml解析错误格式的文档,结果</p>标签被直接忽略掉了:
'''
print '#BeautifulSoup("<a></p>", "lxml"):\n',BeautifulSoup("<a></p>", "lxml")
#BeautifulSoup("<a></p>", "lxml"):
<html><body><a></a></body></html>
'''
#使用html5lib库解析相同文档会得到不同的结果:
'''
print '#BeautifulSoup("<a></p>", "html5lib"):\n',BeautifulSoup("<a></p>", "html5lib")
#html5lib库没有忽略掉</p>标签,而是自动补全了标签,还给文档树添加了<head>标签.
'''

#使用pyhton内置库解析结果如下
'''
print '#BeautifulSoup("<a></p>", "html.parser")\n',BeautifulSoup("<a></p>", "html.parser")
#BeautifulSoup("<a></p>", "html.parser")
#<a></a>
'''
#与lxml [7] 库类似的,Python内置库忽略掉了</p>标签,与html5lib库不同的是标准库没有尝试创建符合标准的文档格式或将文档片段包含在<body>标签内,与lxml不同的是标准库甚至连<html>标签都没有尝试去添加.
#因为文档片段“<a></p>”是错误格式,所以以上解析方式都能算作”正确”,html5lib库使用的是HTML5的部分标准,所以最接近”正确”.不过所有解析器的结构都能够被认为是”正常”的.

#不同的解析器可能影响代码执行结果,如果在分发给别人的代码中使用了 BeautifulSoup ,那么最好注明使用了哪种解析器,以减少不必要的麻烦.
