# -*- coding: utf-8 -*-
import scrapy
from zillow.items import ZillowItem

class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
    #Domain
    allowed_domains = ["https://www.zillow.com"]
    #Get content from the urls
    #Below code will loop through the page numbers twenty times, fetching data from each page
    start_urls = ['https://www.zillow.com/homes/fsbo/LA/mmm_pt/25_rid/globalrelevanceex_sort/40.363288,-82.55127,19.12441,-112.565918_rect/4_zm/%d_p/' % i for i in xrange(1,21,1)] + \
                 ['https://www.zillow.com/homes/fsbo/Davidson-County-TN/mmm_pt/2243_rid/globalrelevanceex_sort/36.498045,-86.316834,35.875141,-87.254792_rect/9_zm/%d_p/' % i for i in xrange(1,17,1)] + \
                 ['https://www.zillow.com/homes/fsbo/WY/mmm_pt/62_rid/globalrelevanceex_sort/46.762443,-100.898438,37.640334,-115.905762_rect/5_zm/%d_p/' % i for i in xrange(1,15,1) ]

    #The response from the pages will be recieved in the following function and it will fetch all the details from particular <li>s though loop
    #and stored in an 'item' array which will return the data to pipeline and pipeline will create a resulting json file.
    def parse(self, response):
        titles = response.selector.css('ul.photo-cards > li')
        for titles in titles:
            item = ZillowItem()
            links = titles.xpath("article/div/a/@href").extract()[0]
            item['link'] = 'https://www.zillow.com'+links
            item['address'] = titles.xpath("article/div/span[@class='hide']/span/text()").extract()
            item['lat_long'] = titles.xpath("article/div/span[2]/meta/@content").extract()
            item['price'] = titles.xpath("article/div/div/p/span[@class='zsg-photo-card-price']/text()").extract()
            item['specs'] = titles.xpath("article/div/div/p/span[@class='zsg-photo-card-info']/text()").extract()
            item['day_on_zillow'] = titles.xpath("article/div/div/p[2]/span[@class='zsg-photo-card-notification ']/text()").extract()
            item['image'] = titles.xpath("article/div/div[@class='zsg-photo-card-img']/img/@src").extract()
            yield (item)



