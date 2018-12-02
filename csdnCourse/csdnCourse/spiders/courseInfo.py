# -*- coding: utf-8 -*-
import scrapy
from csdnCourse.items import CsdncourseItem
from scrapy_redis.spiders import RedisSpider


class CourseinfoSpider(RedisSpider):
    name = 'courseInfo'
    redis_key = "coursespider:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CourseinfoSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = CsdncourseItem()
        item['title'] = response.css("div.qrcode_box_top h1::text").extract_first()
        item['teacher'] = response.css("div.professor_name a::text").extract_first()
        #item['learnnum'] = response.css.re("<span>([0-9]+)人已学习</span>")[0]
        #item['price'] = response.css.re("<sapn class='money'>¥([0-9\.]+)</sapn>")[0]
        print(item)
        yield item
