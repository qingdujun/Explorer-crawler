# -*- coding: utf-8 -*-
import requests
from lxml import etree

class Bugzilla(object):
    def __init__(self):
        self.base_url = 'https://bugs.winehq.org/show_bug.cgi?id=';
        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'};

    def getPage(self, url):
        html = requests.get(url, headers=self.user_agent);
        html.encoding = 'utf-8';
        return html.text;
        
    def getSelector(self, page):
        selector = etree.HTML(page);
        return selector;

    def getUrl(self, number):
        url = self.base_url + str(number);
        return url;

    def getDescription(self, selector):
        description = selector.xpath('//*[@id="c0"]/pre/text()');
        if len(description) <= 0:
            return "";
        return description[0];

    def getComments(self, selector):
        #comments = selector.xpath('//*[@id="comments"]/table/tbody/tr/td/div[position() > 1]/pre/text()');
        #comments = selector.xpath('//*[@class="bz_comment" or not(contains(@id,"c0"))]/pre/text()');
        data = selector.xpath('//*[@class="bz_comment"]/pre');
        comments = [];
        for comms in data:
            comments.append(comms.xpath('string(.)'));
        return comments; #'. '.join(comments);

if __name__ == '__main__':
    bug = Bugzilla();