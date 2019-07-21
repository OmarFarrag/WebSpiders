class CmdParser():

    def __init__(self):
        out_name = self.get_out_file_name()
        out_format = getattr(self,'out-format',None)

    def get_out_file_name(self):
        return getattr(self, 'out', None)
        
    def get_out_file_format(self):
        return getattr(self, 'out-format', None)


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
        super().__init__()
        self.parse_categories()

    # Checks if categories have been passed through cmd args
    # If passed, set `categories_to_crawl` with them
    # Else, set it to default categories
    #
    # Arguments are passed like "-a categories=cat1-cat2-cat3-cat4"
    def parse_categories(self, spider):
        passed_categories = getattr(spider,'categories',None)
        if passed_categories is None :
            self.categories_to_crawl = list(self.default_categories)
        else:
            self.categories_to_crawl = [x.strip() for x in ( passed_categories.split('-') )]
        