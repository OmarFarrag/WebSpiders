# Web Spiders
Web spiders written with Python/Scrapy

# Install Scrapy:
To install scrapy, see https://docs.scrapy.org/en/latest/intro/install.html

# Available spiders:
## Amazon spider:
* Extracts products' reviews, corresponding rating, date, and keywords (categories) of the product
* To run, navigate to the project director and run "scrapy crawl amazonSpider" along with the arguments specified below
* To specify cmd arguments use the format "-a arg=val -a arg2=val2"
* Supported arguments:
    * Categories: The categories to crawl, entered in the format cat1-cat2-cat3. If not entered, default categories will be used
    * out: The name of the output file (without the extension)
    * out-format: The format of output data (csv, json, or xml)

