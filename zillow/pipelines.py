# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
import sys

class ZillowPipeline(object):
    def __init__(self):
        self.file = open('items.js', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

#-------------------------------------------Start SQL Insert----------------------------------------

class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='', db='testdb', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO zillow (link, address, latitude, longitude, price, specs, day_on_zillow, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                           (item['link'].encode('utf-8'),
                            item['address'][0].encode('utf-8'),
                            item['lat_long'][0].encode('utf-8'),
                            item['lat_long'][1].encode('utf-8'),
                            item['price'][0].encode('utf-8'),
                            item['specs'][0]+","+item['specs'][1]+","+item['specs'][2].encode('utf-8'),
                            item['day_on_zillow'][0].encode('utf-8'),
                            item['image'][0].encode('utf-8')
                            )
                           )

            self.conn.commit()
            print "Product Inserted In Databse"


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])


        return item

#=============================End SQL Insert===============================================================
