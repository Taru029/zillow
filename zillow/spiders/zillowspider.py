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
                 ['https://www.zillow.com/homes/fsbo/WY/mmm_pt/62_rid/globalrelevanceex_sort/46.762443,-100.898438,37.640334,-115.905762_rect/5_zm/%d_p/' % i for i in xrange(1,15,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/AK/mmm_pt/3_rid/globalrelevanceex_sort/73.086633,-119.003907,51.206883,-179.033204_rect/3_zm/%d_p/' % i for i in xrange(1,10,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/AL/mmm_pt/4_rid/globalrelevanceex_sort/35.169318,-82.924805,29.969211,-90.428467_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/AZ/mmm_pt/8_rid/globalrelevanceex_sort/39.155622,-104.436036,28.950475,-119.44336_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/CO/mmm_pt/10_rid/globalrelevanceex_sort/41.38093,-101.799317,36.584657,-109.302979_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/FL/mmm_pt/14_rid/globalrelevanceex_sort/33.07313,-76.311036,22.156883,-91.31836_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/GA/mmm_pt/16_rid/globalrelevanceex_sort/35.268046,-79.431153,30.073847,-86.934815_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/IL/mmm_pt/21_rid/globalrelevanceex_sort/44.378839,-81.760254,34.894942,-96.767579_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/IN/mmm_pt/22_rid/globalrelevanceex_sort/42.126747,-82.694092,37.383252,-90.197754_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/Detroit-MI/mmm_pt/17762_rid/globalrelevanceex_sort/42.495137,-82.86438,42.209956,-83.333359_rect/10_zm/%d_p/' % i for i in xrange(1,9,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/Little-Rock-AR/mmm_pt/52998_rid/globalrelevanceex_sort/34.882269,-92.103196,34.5651,-92.572175_rect/10_zm/%d_p/' % i for i in xrange(1,6,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/mmm_pt/globalrelevanceex_sort/34.882269,-92.103196,34.5651,-92.572175_rect/10_zm/%d_p/' % i for i in xrange(1,12,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/WY/mmm_pt/62_rid/globalrelevanceex_sort/45.24782,-103.798829,40.73477,-111.302491_rect/6_zm/%d_p/' % i for i in xrange(1,16,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/AK/mmm_pt/3_rid/globalrelevanceex_sort/73.086633,-119.003907,51.206883,-179.033204_rect/3_zm/%d_p/' % i for i in xrange(1,10,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/AR/mmm_pt/6_rid/globalrelevanceex_sort/37.269681,-88.38501,32.198857,-95.888672_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/CA/mmm_pt/9_rid/globalrelevanceex_sort/42.155259,-111.796875,32.352122,-126.8042_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/CT/mmm_pt/11_rid/globalrelevanceex_sort/42.648101,-70.88379,40.336076,-74.635621_rect/7_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/DC/mmm_pt/12_rid/globalrelevanceex_sort/39.043452,-76.780015,38.743105,-77.248993_rect/10_zm/%d_p/' % i for i in xrange(1,7,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/DE/mmm_pt/13_rid/globalrelevanceex_sort/40.336076,-73.509522,37.942031,-77.261353_rect/7_zm/%d_p/' % i for i in xrange(1,10,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/HI/mmm_pt/18_rid/globalrelevanceex_sort/23.558951,-153.764649,17.785304,-161.268311_rect/6_zm/%d_p/' % i for i in xrange(1,10,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/IA/mmm_pt/19_rid/globalrelevanceex_sort/44.209772,-89.637452,39.618383,-97.141114_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/ID/mmm_pt/20_rid/globalrelevanceex_sort/49.759977,-106.633301,41.120745,-121.640625_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/KS/mmm_pt/23_rid/globalrelevanceex_sort/40.892753,-94.570313,36.062421,-102.073975_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/ME/mmm_pt/28_rid/globalrelevanceex_sort/49.41812,-61.479493,40.722282,-76.486817_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/MS/mmm_pt/34_rid/globalrelevanceex_sort/35.169318,-86.121827,29.969211,-93.625489_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/MT/mmm_pt/35_rid/globalrelevanceex_sort/50.798991,-102.546387,42.334184,-117.553711_rect/5_zm/%d_p/' % i for i in xrange(1,19,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/ND/mmm_pt/37_rid/globalrelevanceex_sort/49.535904,-96.547852,45.363724,-104.051514_rect/6_zm/%d_p/' % i for i in xrange(1,15,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/NE/mmm_pt/38_rid/globalrelevanceex_sort/45.97406,-92.175293,36.730079,-107.182618_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/NH/mmm_pt/39_rid/globalrelevanceex_sort/46.191239,-67.818604,41.750824,-75.322266_rect/6_zm/%d_p/' % i for i in xrange(1,17,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/NM/mmm_pt/41_rid/globalrelevanceex_sort/39.155622,-98.525391,28.950475,-113.532715_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/NV/mmm_pt/42_rid/globalrelevanceex_sort/43.253204,-109.511719,33.605469,-124.519043_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/OK/mmm_pt/45_rid/globalrelevanceex_sort/40.20405,-91.208497,30.135626,-106.215821_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/PR/mmm_pt/48_rid/globalrelevanceex_sort/19.660693,-64.709473,16.728276,-68.461304_rect/7_zm/%d_p/' % i for i in xrange(1,15,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/RI/mmm_pt/50_rid/globalrelevanceex_sort/42.133876,-70.559693,40.978861,-72.435608_rect/8_zm/%d_p/' % i for i in xrange(1,9,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/SD/mmm_pt/52_rid/globalrelevanceex_sort/48.494767,-92.746583,39.647997,-107.753907_rect/5_zm/%d_p/' % i for i in xrange(1,12,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/UT/mmm_pt/55_rid/globalrelevanceex_sort/44.142797,-104.040528,34.624167,-119.047852_rect/5_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/VI/mmm_pt/57_rid/globalrelevanceex_sort/18.777616,-63.899231,17.309998,-65.775147_rect/8_zm/%d_p/' % i for i in xrange(1,3,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/WV/mmm_pt/61_rid/globalrelevanceex_sort/41.298444,-76.431885,36.496389,-83.935547_rect/6_zm/%d_p/' % i for i in xrange(1,21,1) ] + \
                 ['https://www.zillow.com/homes/fsbo/WY/mmm_pt/62_rid/globalrelevanceex_sort/45.24782,-103.798829,40.73477,-111.302491_rect/6_zm/%d_p/' % i for i in xrange(1,16,1) ] 


    #The response from the pages will be recieved in the following function and it will fetch all the details from particular <li>s though loop
    #and store in an 'item' array which will return the data to pipeline and pipeline will create a resulting json file.
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



