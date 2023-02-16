# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Flipkart1Item(scrapy.Item):
    # define the fields for your item here like:
    p_name = scrapy.Field()
    p_price=scrapy.Field()
    p_discount=scrapy.Field()
