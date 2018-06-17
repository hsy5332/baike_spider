# coding: utf-8
from ReptileHtml.baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                print("第%s个URL,爬取的URL是:%s" % (count, new_url))
                html_cont = self.downloader.download(new_url)

                new_urls, new_data = self.parser.parse(self, new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print("当前URL爬取失败,URL连接是:" + str(new_url))

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
