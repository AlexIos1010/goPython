#/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import scrapy

class DomzSpider(scrapy.Spider):
    name = 'dmozer2'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    ]

    def parse(self,response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()

            print title, link, desc
