import unittest
from sentimentscrapper.tests.test_data.html_test_data import HtmlTestData as td
from sentimentscrapper.spiders.amazon_spider import AmazonSpider
from scrapy.http import TextResponse
from scrapy.http import Request

class AmazonSpiderTest(unittest.TestCase):
    
    def setup(self):
        pass

    def test_extract_sub_categories_links(self):    
        amazon_spider = AmazonSpider()
        i=0
        for data, result in td.sub_categories_html.items():
            #TODO : unless the response is instantiated every time, it caches old data 
            response = TextResponse(url = "",encoding="utf8")
            response._set_body(data)
            with self.subTest():
                self.assertEqual(amazon_spider.extract_sub_categories_links(response), result , "data index {}".format(i))
            i=i+1


    def test_extract_products_links(self):
        amazon_spider = AmazonSpider()
        i=0
        for data, result in td.products_links.items():
            #TODO : unless the response is instantiated every time, it caches old data 
            response = TextResponse(url = "",encoding="utf8")
            response._set_body(data)
            with self.subTest():
                self.assertEqual(amazon_spider.extract_products_links(response), result, "data index {}".format(i))
            i = i+1
    
    
    def test_extract_next_pagination(self):
        amazon_spider = AmazonSpider()
        i=0
        for data, result in td.pagination.items():
            #TODO : unless the response is instantiated every time, it caches old data 
            response = TextResponse(url = "",encoding="utf8")
            response._set_body(data)
            with self.subTest():
                self.assertEqual(amazon_spider.extract_next_pagination(response), result, "data index {}".format(i))
            i = i+1
    
    
    def test_see_all_reviews(self):
        amazon_spider = AmazonSpider()
        response = TextResponse(url = "",encoding="utf8")
        response._set_body("<a href=\"/pass\">all revs See now </a>")
        result = next(amazon_spider.see_all_reviews(response))
        #self.assertIs(result, generator)
        self.assertIsInstance(result, Request)
        self.assertEqual(result.url, amazon_spider.base_url+"/pass"
        )
    

    if __name__ == '__main__' :   
        unittest.main()