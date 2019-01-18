from bs4 import BeautifulSoup
import re
from urllib import parse


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        tem_urls=set()
        # <a target="_blank" href="/item/TIOBE">TIOBE</a>
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            tem_urls.add(new_full_url)
        return tem_urls

    def _get_new_data(self, page_url, soup):

        res_data = {}

        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        # </dd>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title")
        res_data['title'] = title_node.get_text()
        # <div class="para" label-module="para"></div>
        summary_node = soup.find('div', class_="para")
        res_data['summary'] = summary_node.get_text()
        return res_data

