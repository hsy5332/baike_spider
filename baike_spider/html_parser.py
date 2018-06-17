# coding: utf-8
import bs4
import re
from urllib.parse import urljoin


class HtmlParser(object):
    def get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)  # 获取到不完整的URL，然后用urlparse 方法把URL拼接完整
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()  # 获取页面标题
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()  # 获取爬取的内容
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        else:
            soup = bs4.BeautifulSoup(html_cont, 'html.parser')
            new_urls = HtmlParser().get_new_urls(page_url, soup)
            new_data = HtmlParser().get_new_data(page_url, soup)
            return new_urls, new_data
