# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from unicodedata import name
import scrapy


class HomeAssignementItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rank = scrapy.Field()
