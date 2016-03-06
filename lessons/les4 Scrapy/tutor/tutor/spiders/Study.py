#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import scrapy
from scrapy.selector import Selector
from tutor.items import StudyItem

class StudySpider(scrapy.Spider):
    name = 'Study'
    allowed_domains = ['jianshu.com']
    start_urls = [
        "http://www.jianshu.com/collection/a6da567d3276"
    ]

    def parse(self,response):
        sels = response.xpath('//ul/li[@class="avatar"]')
        items = []
        for sel in sels:
            item['title'] = sel.xpath('@data-nickname').extract()        
            item['link'] = sel.xpath('@src').extract()        
            items.append(item)
            print name
            print imgurl,'\n'

