#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

from bs4 import BeautifulSoup

def get_h2_from_next_div_has_h2(tag):
    list = [];
    for next_div in tag.find_next_siblings('div'):
        has_h2Set = next_div.find_all('h2')
        list = list + has_h2Set
    return list

def get_h3_from_next_div_has_h3(tag):
    list = [];
    for next_div in tag.find_next_siblings('div'):
        has_h3Set = next_div.find_all('h3')
        list = list + has_h3Set
    return list

fname = '1.html'#raw_input('Open file:')

try:
    print '\nOpen file\n'
    html_f = open('%s'%fname,'r+')

    content_f = open('bsWebcontent.txt','w')
    print '\nBuild Content File'

    soup = BeautifulSoup(html_f)
    h1_tagSet = soup.find_all('h1')
    h1_count = 0
    for h1_tag in h1_tagSet:
        h1 = h1_tag.get_text()
        print '\n#%d '%h1_count,h1
        h1_encode = '\n#%d '%h1_count+ h1.encode('utf-8') + '\n'
        print 'h1_encode:',h1_encode
        content_f.write(h1_encode)
        h2Set = get_h2_from_next_div_has_h2(h1_tag)
        h2_count = 0
        for h2 in h2Set:
            print '##%d.%d'%(h1_count,h2_count),h2.get_text()
            h2_encode = '##%d.%d '%(h1_count,h2_count) + h2.get_text().encode('utf-8') + '\n'
            content_f.write(h2_encode)
            h3Set = get_h3_from_next_div_has_h3(h2)
            h3_count = 0
            for h3 in h3Set:
                print '###%d.%d.%d'%(h1_count,h2_count,h3_count),h3.get_text()
                h3_encode = '###%d.%d.%d '%(h1_count,h2_count,h3_count)+ h3.get_text().encode('utf-8') + '\n'
                content_f.write(h3_encode)
                h3_count += 1
            h2_count += 1
#        raw_input('Next')
        h1_count += 1

    content_f.close()
    print '\nContent File Saved'
    html_f.close()
    print '\nHtml File closed\n'
except Exception,e:
    print 'Exp Caught'
    print e.__class__
