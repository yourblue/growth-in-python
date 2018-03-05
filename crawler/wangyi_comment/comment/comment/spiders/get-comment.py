import scrapy


class Comment_Get(scrapy.Spider):
    name = 'comment-get'
    start_urls = [
        "http://music.163.com/#/song?id=531040860"
    ]

    def parse(self, response):
        pass
