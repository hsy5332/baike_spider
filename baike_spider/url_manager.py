# coding: utf-8

class UrlManger(object):
    def __init__(self):
        self.new_urls = set()  # 创建集合来存储爬取的新URL和旧URL
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)  # 判断URL是否使用过，没有使用过则加入new URL 集合中

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()  # 获取URL 并删除
        self.old_urls.add(new_url)
        return new_url
