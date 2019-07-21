class CmdParser():

    def __init__(self, spider):
        self.spider = spider
    
    def parse(self):
        self.parse_out_file_name()
        self.parse_out_file_format()

    def parse_out_file_name(self):
        self.spider.out_name = getattr(self.spider, 'out', 'out')
        
    def parse_out_file_format(self):
        self.spider.put_format = getattr(self.spider, 'out-format', 'csv')


class AmazonCmdParser(CmdParser):

    default_categories = [
        "Arts & Crafts" , "Automotive", "Baby", 
        "Beauty & Personal Care", "Books", "computers",
        "Electronics", "Women's Fashion", "Men's Fashion",
        "Girl's Fashion", "Boy's Fashion", "Health & Household",
        "Home & Kitchen", "Industrial & Scientific", "Luggage",
        "Movies & Television", "Music, CDs & Vinyl", "Pet Supplies",
        "Software", "Support & Outdoors", "Tools & Home Improvement",
        "Toys & Games", "Video Games"
    ]


    def __init__(self, spider):
        super().__init__(spider)
    
    def parse(self):
        super().parse()
        self.parse_categories()

    # Checks if categories have been passed through cmd args
    # If passed, set `categories_to_crawl` with them
    # Else, set it to default categories
    #
    # Arguments are passed like "-a categories=cat1-cat2-cat3-cat4"
    def parse_categories(self):
        passed_categories = getattr(self.spider,'categories',None)
        if passed_categories is None :
            self.spider.categories_to_crawl = list(self.default_categories)
        else:
            self.spider.categories_to_crawl = [x.strip() for x in ( passed_categories.split('-') )]
        