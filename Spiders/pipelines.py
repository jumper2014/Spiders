# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class SpidersPipeline:
    def process_item(self, item, spider):
        return item


class DoubanMovieTop250Pipeline:
    def process_item(self, item, spider):
        """处理爬虫传过来的数据
        将item进行json处理后, 保存到指定的文件中
        Arguments:
            item {dict} -- 数据的item对象
            spider {object} -- 产生item数据的爬虫
        Returns:
            dict -- Item对象
        """
        file_path = './out/douban.txt'
        with open(file_path, 'a', encoding="utf-8") as f:
            f.write(item["ranking"] + "," + item["movie_name"] + "\n")
        return item
