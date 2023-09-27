# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JumiaphoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JumiaItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    seller_name = scrapy.Field()
    seller_score = scrapy.Field()
    followers = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    
