# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from settings import MYSQL_URL


class Qufen2CouponsPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(MYSQL_URL)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):

        return item
