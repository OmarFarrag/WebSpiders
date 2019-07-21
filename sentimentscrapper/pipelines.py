# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import *
from scrapy.exceptions import DropItem

class AmazonReviewsVerificationPipeline(object):
    def process_item(self, item, spider):
        if item.get('stars'):
            if item.get('comment'):
                if item.get('date'):
                    print(item)
                    return item
                else:
                    raise DropItem("Missing date")
            else:
                raise DropItem("Missing comment")
        else:
            raise DropItem("Missing stars")
        


class ExportPipeline(object):
    """  """
    formats_exporters = {
        'json' : JsonItemExporter,
        'xml' : XmlItemExporter,
        'csv' : CsvItemExporter
    }

    def open_spider(self, spider):
        f = open('{}.{}'.format(spider.out_name, spider.out_format),'wb')
        self.exporter = self.formats_exporters[spider.out_format](f)
        print("******************")
        print(self.exporter)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()


