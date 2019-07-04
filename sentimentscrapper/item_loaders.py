from scrapy.loader import ItemLoader
from sentimentscrapper.items import AmazonReviewItem
from scrapy.loader.processors import MapCompose

def filter_rating(self,txts):
    for txt in txts:
        yield float(txt.split()[0])*0.2


class AmazonReviewLoader(ItemLoader):
    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        self.default_item_class = AmazonReviewItem
        return super().__init__(item=item, selector=selector, response=response, parent=parent, **context)
    
    stars_in = filter_rating
