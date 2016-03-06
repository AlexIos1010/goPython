#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import scrapy

class StudySpider(scrapy.Spider):
    name = 'Study'
    allowed_domains = ['http://www.jianshu.com/collection/a6da567d3276']
    start_urls = [
        "http://www.jianshu.com/collection/a6da567d3276"
    ]

    def parse(self,response):
        sels = response.xpath('//ul/li[@class="avatar"]')
        for sel in sels:
            name = sel.xpath('@data-nickname').extract()        
            imgurl = sel.xpath('@src').extract()        
            print name
            print imgurl,'\n'

