import scrapy
from ..items import ScrapyDoubanMovieTop250Item

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        movie_list = response.xpath('//*[@class="item"]')
        playable_true = '[可播放]'
        playable_false = '[不可播放]'
        for movie in movie_list:
            #定义movie_item成为scrapy的item
            movie_item = ScrapyDoubanMovieTop250Item()
            movie_item['rank'] = movie.xpath('./div[@class="pic"]/em/text()').get()
            movie_item['title'] = movie.xpath('./div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').get()
            movie_item['cover'] = movie.xpath('./div[@class="pic"]/a/img/@src').get()
            playable = movie.xpath('./div[@class="info"]/div[@class="hd"]/span[2]').get()
            if playable == playable_true:
                movie_item['playable'] = playable_true
            else:
                movie_item['playable'] = playable_false
            info_line1 = movie.xpath('./div[@class="info"]/div[@class="bd"]/p[1]/text()[1]').get().strip().split('\xa0\xa0\xa0')
            info_line2 = movie.xpath('./div[@class="info"]/div[@class="bd"]/p[1]/text()[2]').get().strip().split('\xa0/\xa0')
            movie_item['director'] = str(info_line1[0])
            movie_item['starring'] = str(info_line1[-1])
            movie_item['release_date'] = str(info_line2[0])
            movie_item['country'] = str(info_line2[1])
            movie_item['genre'] = str(info_line2[2])
            movie_item['mark'] = movie.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').get()
            movie_item['rater'] = movie.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').get()
            yield movie_item

            next_page = response.xpath('//span[@class="next"]/a/@href').get()
            if next_page:
                yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)


