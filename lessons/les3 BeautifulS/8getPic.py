#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex


import urllib2

from bs4 import BeautifulSoup


def ul_li_a_img(tag):
    pTag = tag.parent
    ppTag = pTag.parent
    pClass = ppTag.get('id')
    raw_input ('pClass')
    print pClass
    '''
    if pClass == ['blog_userface']:
        raw_input ('def1')
        print 'tag',tag
        return tag
    '''

#parse [<img src=url> set]
def get_url_from_img(imgSet):
    urlL = []
    for img in imgSet:
        url = img.get('src')
        urlL.append(url)
    raw_input ('def2')
    print 'urlL',urlL
    return urlL


url = "http://blog.csdn.net/yunhuang2010/article/details/24413249"
user_agent = ''#Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36{'User-Agent':}
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html_doc = response.read().decode('utf-8')
    soup = BeautifulSoup(html_doc)
    imgSet = soup.find_all(ul_li_a_img)
    urlList = get_url_from_img(imgSet) 

    picname = raw_input ('Input img name prefix:')
    count = 1
    for url in urlList:
        f = open('./download/%s%d.jpg'%(picname,count),'wb')
        img = urllib2.urlopen(url).read()
        f.write(img)
        f.close()
        print 'Saved%d',count
        count += 1

except urllib2.URLError,e:
    if hasattr(e,"code"):
        print "\nExp Code:",e.code
    if hasattr(e,"reason"):
        print "\nExp reason:",e.reason


