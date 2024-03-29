# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonReviewItem(scrapy.Item):
    # The main comment
    comment = scrapy.Field()
    # No of starts out of 5
    stars = scrapy.Field()
    # Example : ['Electronics','PC','Accessories','Keyboards']
    # Might be useful later if we want to filter some data
    keywords = scrapy.Field()
    date = scrapy.Field()
