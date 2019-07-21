from sentimentscrapper.exceptions import *


class CmdParser():

    # TODO: Move to another place
    formats = [
        'json',
        'xml',
        'csv' 
    ]

    def __init__(self, spider):
        self.spider = spider
    
    def print_description(self):
        print("""
        out             The name of the output file
        out-format      The format of output data\
        """
        )
    
    def parse(self):
        try:
            self.parse_out_file_name()
            self.parse_out_file_format()
        except (InvalidOutFormat, MissingArgument) as e:
            e.print_description()
            raise
               
    def parse_out_file_name(self):
        self.spider.out_name = getattr(self.spider, 'out', 'out')
        
    def parse_out_file_format(self):
        # TODO: change this missing thing
        out_format = getattr(self.spider, 'out-format', 'missing').lower()
        if out_format == "missing":
            raise MissingArgument
        elif out_format not in self.formats:
            raise InvalidOutFormat
        else:
            self.spider.out_format = out_format


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

    def print_description(self):
        super().print_description()
        print(
        """\
        categories      The categories to crawl separated by a '-'
        """)
    
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
        