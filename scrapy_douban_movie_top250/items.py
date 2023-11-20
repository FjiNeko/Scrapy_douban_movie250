# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanMovieTop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    playable = scrapy.Field()
    director = scrapy.Field()
    starring = scrapy.Field()
    release_date = scrapy.Field()
    country = scrapy.Field()
    genre = scrapy.Field()
    mark = scrapy.Field()
    rater = scrapy.Field()