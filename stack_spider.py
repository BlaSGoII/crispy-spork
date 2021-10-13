#!usr/bin/env python3

from scrapy import Spider

class StackSpider (Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath('//div[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath('//div[@class="question-hyperlink"]/@href').extract()[0]
            yield item
