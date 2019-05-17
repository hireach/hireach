# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparam = {
            'host': '127.0.0.1',
            'port':3306,
            'user': 'root',
            'password': 'mysql',
            'database': 'jianshu',
            'charset': 'utf8'

        }
        self.conn = pymysql.connect(**dbparam)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self._sql,(item['title'],item['author'],item['pub_time'],item['acticle_id'],item['content']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into jianshu(id,title,author,pub_time,acticle_id,content) values(null,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql

class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparam = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'mysql',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass':cursors.DictCursor

        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparam)
        self._sql = None

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_err,item,spider)
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
               insert into jianshu(id,title,author,pub_time,acticle_id,content) values(null,%s,%s,%s,%s,%s)
               """
            return self._sql
        return self._sql

    def insert_item(self,cursor,item):
        cursor.execute(self._sql,(item['title'], item['author'], item['pub_time'], item['acticle_id'], item['content']))

    def handle_err(self,error,item,spider):
        print('='*10+'erro'+'='*10)
        print(error)
        print('='*10+'erro'+'='*10)
