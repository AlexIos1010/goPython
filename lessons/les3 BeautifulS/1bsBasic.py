#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<a href="http://example.com/tillie" class="bro" id="link3">Alex</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""
soup = BeautifulSoup(html_doc)
############################################
#                                          #
#           Basic Use                      #
#                                          #
############################################
#print soup.title

#print type(soup.title)

#print soup.title.name

#print soup.title.string

#print soup.p

"""
atag = soup.a

print 'atag:',atag
print 'type(atag):',type(atag)
aText = atag.get_text()
aText2 = atag.string
aText3 = atag['class']

print 'aText = atag.get_text()'
print 'type(aText):',type(aText)
print 'aText:',aText

print '\naText2 = atag.string'
print 'type(aText2):',type(aText2)
print 'aText2:',aText2

print "\naText3 = atag['class']"
print 'type(aText3):',type(aText3)
print 'aText3:',aText3

"""

#print atag.name

#print atag.attrs

#print atag.get_text()

'''
allLink = soup.find_all('a')

for link in allLink:
    lText = link.get_text()
#    print lText
    lClass = link['class']
    print lClass
#    lClass2 = link.get('class')
#    print lClass2
    if (lClass==['sister']):
        print 'sister:',lText
'''
#print soup.find_all('a')

#print soup.find(id='link3')

#print soup.get_text()

'''
for link in soup.find_all('a'):
    print(link.get('href'))
   # http://example.com/elsie
   # http://example.com/lacie
   # http://example.com/tillie
'''

############################################
#          
#       .contents 和 .children 
#   tag的 .contents 属性可以将tag的子节点以列表的方式输出:
#          
#           
############################################
'''
p_tag = soup.find_all('p')
print 'p_tag type:',type(p_tag)
print 'len(p_tag):',len(p_tag)
count = 1
for ptag in p_tag:
    print 'type(ptag):',type(ptag)
    print 'ptag%d:'%count,ptag
    ptag_contents = ptag.contents
    raw_input('Show .contents')
    print 'ptag_contents type:',type(ptag.contents)
    print 'ptag_contents:',ptag.contents
    for content in ptag_contents:
        print 'content type:',type(content)
        print 'content:',content

    ptag_children = ptag.children
    raw_input('Show .children')
    print 'ptag_children type:',type(ptag.children)
    print 'ptag_children:',ptag.children

    raw_input('Next')
    count += 1
'''

############################################
#          
#       .strings 和 stripped_strings
#   如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取
#   输出的字符串中可能包含了很多空格或空行,
#                使用 .stripped_strings 可以去除多余空白内容        
#           
############################################
'''
strs = soup.get_text()
strings = soup.strings
stripstr = soup.stripped_strings

print 'strs = soup.get_text()'
print 'strs type:',type(strs)
print 'strs:',strs

print 'strings = soup.strings'
print 'strings type:',type(strings)
print 'strings:',strings
for string in strings:
    print 'string type:',type(string)
    print 'string:',string
    raw_input('Next')

print 'stripstr = soup.stripped_strings'
print 'stripstr type:',type(stripstr)
print 'stripstr:',stripstr
for string in stripstr:
    print 'string type:',type(string)
    print 'string:',string
    raw_input('Next')
'''



############################################
#          
#       过滤器 
#   过滤器贯穿整个搜索的API.过滤器可以被用在tag的name中,
#               节点的属性中,字符串中或他们的混合中.
#           
#  1.字符串 2.正则表达式 3.列表 4.True 5.方法           
#
############################################

#1.字符串
#最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签:
'''
print soup.find_all('b')
#[<b>The Dormouse's story</b>]
'''

#2.正则表达式
#如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
'''
for tag in soup.find_all(re.compile('^b')):
    print tag.name
#body
#b
'''

#3.列表
#如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签:
'''
for tag in soup.find_all(['a','b']):
    print '#',tag.name
# b
# a
# a
# a
# a
'''

#4.True
#True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
'''
for tag in soup.find_all(True):
    print '#',tag.name
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# a
# p
'''

#5.方法
#如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False

#下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
'''
def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
for tag in soup.find_all(has_class_no_id):
    print '#',tag

# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
#<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
#<a class="bro" href="http://example.com/tillie" id="link3">Alex</a>;
#and they lived at the bottom of a well.</p>
# <p class="story">...</p>
'''


############################################
#          
#           find_all()
#   find_all( name , attrs , recursive , text , **kwargs )
#          
#          
############################################

#name 参数
#name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.
#简单的用法如下:
'''
print '#',soup.find_all("title")
# [<title>The Dormouse's story</title>]
'''
#keyword 参数
##如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
'''
print '#',soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
'''

##使用多个指定名字的参数可以同时过滤tag的多个属性:
'''
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
'''
##有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
'''
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression
'''
##但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
'''
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
'''

#按CSS搜索
##按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag:
'''
print '#',soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''

##class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True :
'''
print '#',soup.find_all(class_=re.compile('itle'))
# [<p class="title"><b>The Dormouse's story</b></p>]
'''
'''
def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
print '#',soup.find_all(class_=has_six_characters)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''

##搜索 class 属性时也可以通过CSS值完全匹配:
'''
print '#',css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]
'''

##完全匹配 class 的值时,如果CSS类名的顺序与实际不符,将搜索不到结果:
'''
soup.find_all("a", attrs={"class": "sister"})
'''

#text 参数
#通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True . 看例子:
'''
soup.find_all(text="Elsie")
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
# [u"The Dormouse's story", u"The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    ""Return True if this string is the only child of its parent tag.""
    return (s == s.parent.string)

soup.find_all(text=is_the_only_string_within_a_tag)
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']
'''

#limit 参数
#find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.

#文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量:
'''
#soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
'''

#recursive 参数
#调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False
#是否使用 recursive 参数的搜索结果:
'''
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]

soup.html.find_all("title", recursive=False)
# []
'''

#像调用 find_all() 一样调用tag¶
#find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 find_all() 方法相同,下面两行代码是等价的:
'''
soup.find_all("a")
soup("a")
'''

############################################
#                                 
#          CSS选择器
#   Beautiful Soup支持大部分的CSS选择器,
#    在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数,
#    即可使用CSS选择器的语法找到tag
#            
############################################
'''
print '#',soup.select("title")
# [<title>The Dormouse's story</title>]
'''

#通过tag标签逐层查找:
'''
print '#',soup.select("p a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, <a class="bro" href="http://example.com/tillie" id="link3">Alex</a>]
'''

#找到某个tag标签下的直接子标签
'''
soup.select("head > title")
# [<title>The Dormouse's story</title>]

print '#',soup.select("p > a:nth-of-type(3)")
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
'''

#通过CSS的类名查找:
'''
print '#',soup.select(".sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''

#通过tag的id查找:
'''
print '#',soup.select("#link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
'''

#通过属性的值来查找:
'''
print '#',soup.select('a[href="http://example.com/elsie"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
'''

#通过语言设置来查找:

multilingual_markup = """
<p lang="en">Hello</p>
<p lang="en-us">Howdy, y'all</p>
<p lang="en-gb">Pip-pip, old fruit</p>
<p lang="fr">Bonjour mes amis</p>
"""
multilingual_soup = BeautifulSoup(multilingual_markup)
print '#',multilingual_soup.select('p[lang|=en]')
# [<p lang="en">Hello</p>, <p lang="en-us">Howdy, y'all</p>, <p lang="en-gb">Pip-pip, old fruit</p>]
