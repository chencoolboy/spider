# -*- coding: utf-8 -*-
import scrapy
import re
from manhua_spider.items import ManhuaSpiderItem
from scrapy.http import Request
from selenium import webdriver
from bs4 import BeautifulSoup


class HaizeiwangSpider(scrapy.Spider):
    name = 'haizeiwang'
    allowed_domains = ['manhua.fzdm.com/002/Vol_001']
    start_urls = ['http://manhua.fzdm.com/002/Vol_001/']

    def parse(self, response):
        item=ManhuaSpiderItem()
        path = "E:/360Downloads/geckodriver"
        browser = webdriver.Firefox(executable_path=path)
        list=[]
        try:
            for i in range(0,150):
                url = response.url+"index_" + str(i) + ".html"
                browser.get(url)
                sourcepage = browser.page_source
                soup = BeautifulSoup(sourcepage, "lxml")
                imageurl = soup.find_all(id="mhpic")
                pat = ' src="(.*?)"'
                picurl = re.compile(pat).findall(str(imageurl))
                list.append(picurl[0])
        except Exception as e:
            pass
        browser.quit()
        item["image_url"]=list
        print(item["image_url"])
        yield item
        for i in range(2,36):
            if i <= 9:
                this_chapter_url = 'http://manhua.fzdm.com/002/Vol_00' + str(i)
            elif 9 < i <= 35:
                this_chapter_url = 'http://manhua.fzdm.com/002/Vol_0' + str(i)
            yield Request(this_chapter_url,callback=self.parse,dont_filter=True)
        for i in range(337,898):
            this_chapter_url = 'http://manhua.fzdm.com/002/' + str(i)
            yield Request(this_chapter_url,callback=self.parse,dont_filter=True)