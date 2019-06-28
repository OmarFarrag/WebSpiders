import scrapy
import logging

class AmazonSpider(scrapy.Spider):

    name = "amazonSpider"

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

    # The base url of the website that we append the categories' hrefs to 
    base_url = 'https://www.amazon.com'
    
    # Link to the categories page
    # From this page will start crawling each category and its sub categories    
    categories_url = "https://www.amazon.com/b?node=17938598011"
    
    # Boolean used to idengtify the first response as it has
    # different parsing than other responses
    initial_response = True

    # List of the categories to be crawled
    # Set to run time either to user specified or default categories
    categories_to_crawl = []


    # Checks if categories have been passed through cmd args
    # If passed, set `categories_to_crawl` with them
    # Else, set it to default categories
    #
    # Arguments are passed like "-a categories = cat1-cat2-cat3-cat4"
    def parse_cmd_args(self):
       # Get the categoriess passed as cmd args
        passed_categories = getattr(self,'categories',None)
        if passed_categories is None :
            self.categories_to_crawl = list(self.default_categories)
        else:
            self.categories_to_crawl = [x.strip() for x in ( passed_categories.split('-') )]
      


    # This function checks if there are sub-categories within the category we are right now.
    # If there is at least one category, it returns a list of these sub-categorie
    def check_for_categories(self,response):
        pass


    # First functions gets execution
    # Yileds requests to the main categories 
    def start_requests(self):
        self.parse_cmd_args()
        yield scrapy.Request(self.categories_url, self.parse)


    # Parses the initial page of categories, "Departments" page
    # Returns a dictionary with the categories names as keys and their links as values
    def extract_categories_links(self, response):
        links = response.css('div.left_nav a::attr(href)').getall()
        categories = response.css('div.left_nav a::text').getall()
        categories_links_dict = dict(zip(categories,links))   
        # Remove unselected categories
        categories_links_dict = { k:v for k,v in categories_links_dict.items() if k in self.categories_to_crawl }
        return categories_links_dict


    # Parses sub categories and return a list with the sub 
    # categories names as keys and their links as values. If no 
    # sub categories exist, returns empty list []
    def extract_sub_categories_links(self, response):
        subCategories_links = response.xpath("//li/span/a[contains(@href,\"?i\")][span[contains(@class,\"a-color-base\")]]/@href").getall()
        if not subCategories_links:
            return []
        return subCategories_links

    # The main parser of all requests
    #
    # 1- Check for the first response as it has different parsing
    #    If so, yield requests for the categories specified in [categories_to_crawl]
    #
    # 2- Navigate to sub-categories until there are no more sub-categories 
    def parse(self, response): 

        if self.initial_response==True:
            categories_links_dict = self.extract_categories_links(response)
            for category, link in categories_links_dict.items():
                yield scrapy.Request(self.base_url+link, callback = self.parse)    
            self.initial_response = False
            return

        sub_categories_links = self.extract_sub_categories_links(response)