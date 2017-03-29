# zillow_scrapy

# Getting Started

# Firstly you have to install python version 2.7.0
# Intall scrapy version 1.2.1
# Import the database file - "testdb.sql" on your localhost
# After installing scrapy, you can check scrapy version version "scrapy version" at your terminal
# After checking the version navigate to the folder where you have placed your scrapy folder
# Open "pipelines.py" file and change the database settings.
# Reaching the root of the scrapy folder you can execute following command
# scrapy crawl zillowspider and press enter
# If you get "TypeError: 'float' object is not iterable" error, execute 'pip install Twisted==16.4.1' command on your terminal
# Again execute scrapy crawl zillowspider and press enter
# You will get all the listing on your terminal as well as a json - "items.js" file will created at the root of your scrapy folder
# containing all the records.
