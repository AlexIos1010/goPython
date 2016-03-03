#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex


import urllib2

from bs4 import BeautifulSoup


url = raw_input('Input site you want ')
user_agent = ''#Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36{'User-Agent':}
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html_doc = response.read().decode('utf-8')
#    print html_doc
    soup = BeautifulSoup(html_doc)
#    print soup.find(id='hlogo')
#    print soup.img
    imgDiv = soup.find_all('img')
    print len(imgDiv)
    picname = raw_input('picname:')
    picnum = 1
    for image in imgDiv:
        imgUrl = image.get('src')
        print imgUrl
        tmp = urllib2.urlopen(imgUrl)
        tmpB = tmp.read()
        imgF = open('./download/%s%d.jpg'%(picname,picnum),'wb')
        imgF.write(tmpB)
        imgF.close()
        print 'Saved'
        raw_input('Next')

except urllib2.URLError,e:
    if hasattr(e,"code"):
        print "\nExp Code:",e.code
    if hasattr(e,"reason"):
        print "\nExp reason:",e.reason
    

