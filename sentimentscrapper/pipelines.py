# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AmazonReviewsVerificationPipeline(object):
    def process_item(self, item, spider):
        if item.get('stars'):
            if item.get('comment'):
                if item.get('date'):
                    return item
                else:
                    raise DropItem("Missing date")
            else:
                raise DropItem("Missing comment")
        else:
            raise DropItem("Missing stars")
        
