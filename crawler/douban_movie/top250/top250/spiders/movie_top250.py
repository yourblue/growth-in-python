from scrapy import Request
from scrapy.spiders import Spider
from top250.items import Top250Item


class GetMovie(Spider):
    name = 'movie'
    start_urls = {
        'https://movie.douban.com/top250'
    }

    def parse(self, response):
        item = Top250Item()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        print(movies)
        print('===========================')
        for movie in movies:
            # print('===={0}===='.format(movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()))
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()
            item['movie_name'] = movie.xpath('.//div[@'
                                             '="hd"]/a/span[1]/text()').extract()
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url)
