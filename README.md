# Web Spiders
Web spiders written with Python/Scrapy

# Install Scrapy:
To install scrapy, see https://docs.scrapy.org/en/latest/intro/install.html

# Available spiders:
## Amazon spider:
* Extracts products' reviews, corresponding rating, date, and keywords (categories) of the product
* To run, navigate to the project director and run "scrapy amazonSpider", this will navigate through all categories by default
* To specify specific categories, use "-a categories=cat1-cat2-cat3"
* All extracted data is exported to a csv file "amazon_reviews.csv" in the same directory of the spider
