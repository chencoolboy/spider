# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
class ManhuaSpiderPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item["image_url"])):
            file="D:/爬虫/海贼王漫画/"+str(i)+".jpg"
            urllib.request.urlretrieve(item["image_url"][i], file)
        return item
