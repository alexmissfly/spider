import html_downloader
import html_outputer
import html_parse
import url_manange


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manange.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parse.HtmlParser()
        self.output = html_outputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('crow %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)

                if count == 10:
                    break

                count = count + 1
            except:
                print('craw failed')
        self.output.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
