#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Alex

import scrapy

class DmozSpider(scrapy.Spider):
    name = 'dmozer'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self,response):
        filename = response.url.split("/")[-2]+'.html'
        with open(filename,'wb') as f:
            f.write(response.body)
