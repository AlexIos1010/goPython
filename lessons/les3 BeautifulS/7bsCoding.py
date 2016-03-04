#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

from bs4 import BeautifulSoup

from bs4 import UnicodeDammit

#任何HTML或XML文档都有自己的编码方式,比如ASCII 或 UTF-8,但是使用Beautiful Soup解析后,文档都被转换成了Unicode:
'''
markup = "<h1>Sacr\xc3\xa9 bleu!</h1>"
soup = BeautifulSoup(markup)
print '#',soup.h1
print '#',type(soup.h1.string)
'''

#Beautiful Soup用了 编码自动检测 子库来识别当前文档编码并转换成Unicode编码. BeautifulSoup 对象的 .original_encoding 属性记录了自动识别编码的结果:
'''
print '#',soup.original_encoding
'''

#输出编码
#通过Beautiful Soup输出文档时,不管输入文档是什么编码方式,输出编码均为UTF-8编码,下面例子输入文档是Latin-1编码:

markup = '''
    <html>
      <head>
          <meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
            </head>
              <body>
                  <p>Sacr\xe9 bleu!</p>
                    </body>
                    </html>
'''

soup = BeautifulSoup(markup)
#print(soup.prettify())

#如果不想用UTF-8编码输出,可以将编码方式传入 prettify() 方法:
#还可以调用 BeautifulSoup 对象或任意节点的 encode() 方法,就像Python的字符串调用 encode() 方法一样:
'''
print(soup.prettify("latin-1"))
print(soup.encode('latin-1'))
<html>
 <head>
  <meta content="text/html; charset=latin-1" http-equiv="Content-type"/>
 </head>
 <body>
  <p>
   Sacré bleu!
  </p>
 </body>
</html>

<html>
<head>
<meta content="text/html; charset=latin-1" http-equiv="Content-type"/>
</head>
<body>
<p>Sacré bleu!</p>
</body>
</html>
'''

#如果文档中包含当前编码不支持的字符,那么这些字符将呗转换成一系列XML特殊字符引用,下面例子中包含了Unicode编码字符SNOWMAN:

markup = u"<b>\N{SNOWMAN}</b>"
snowman_soup = BeautifulSoup(markup)
tag = snowman_soup.b
'''
print '#tag:',tag
#tag: <b>☃</b>

print '#',tag.encode('utf-8')
# <b>☃</b>
'''

#SNOWMAN字符在UTF-8编码中可以正常显示(看上去像是☃),但有些编码不支持SNOWMAN字符,比如ISO-Latin-1或ASCII,那么在这些编码中SNOWMAN字符会被转换成“&#9731”:
'''
print(tag.encode("utf-8"))
print tag.encode("latin-1")
print tag.encode("ascii")
<b>☃</b>
<b>&#9731;</b>
<b>&#9731;</b>
'''

#Unicode, dammit! 
#编码自动检测 功能可以在Beautiful Soup以外使用,检测某段未知编码时,可以使用这个方法:
'''
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
# Sacré bleu!
print dammit.original_encoding
# 'utf-8'
'''


#矛盾的编码
#有时文档的大部分都是用UTF-8,但同时还包含了Windows-1252编码的字符,就像微软的智能引号 [10] 一样.一些包含多个信息的来源网站容易出现这种情况. UnicodeDammit.detwingle() 方法可以把这类文档转换成纯UTF-8编码格式,看个简单的例子:

snowmen = (u"\N{SNOWMAN}" * 3)
quote = (u"\N{LEFT DOUBLE QUOTATION MARK}I like snowmen!\N{RIGHT DOUBLE QUOTATION MARK}")
doc = snowmen.encode("utf8") + quote.encode("windows_1252")

#这段文档很杂乱,snowmen是UTF-8编码,引号是Windows-1252编码,直接输出时不能同时显示snowmen和引号,因为它们编码不同:
'''
print '#',(doc)
# âââI like snowmen!

print '#',(doc.decode("windows-1252"))
# Traceback (most recent call last):
  File "7bsCoding.py", line 112, in <module>
    print '#',(doc.decode("windows-1252"))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-9: ordinal not in range(128)
'''

#如果对这段文档用UTF-8解码就会得到 UnicodeDecodeError 异常,如果用Windows-1252解码就回得到一堆乱码.幸好, UnicodeDammit.detwingle() 方法会吧这段字符串转换成UTF-8编码,允许我们同时显示出文档中的snowmen和引号:

'''
new_doc = UnicodeDammit.detwingle(doc)
print(new_doc)

☃☃☃“I like snowmen!”
'''
