# -*- coding: utf-8 -*-
import requests
from lxml import etree
from ..mysql.database import db

class Bugzilla(object):
    def __init__(self):
        self.base_url = 'https://bugs.winehq.org/show_bug.cgi?id=';
        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'};

    def getUrl(self, number):
        url = self.base_url + str(number);
        return url;

    def getPage(self, url):
        html = requests.get(url, headers=self.user_agent);
        html.encoding = 'utf-8';
        return html.text;
        
    def getSelector(self, page):
        return etree.HTML(page);

    def getTitle(self, selector):
        title = selector.xpath('//*[@id="main_content"]/div/div/h2/text()');
        return title[0] if len(title) > 0 else "";

    def getDescription(self, selector):
        description = selector.xpath('//*[@id="c0"]/pre/text()');
        return description[0] if len(description) > 0 else "";

    def getComments(self, selector):
        data = selector.xpath('//*[@class="bz_comment"]/pre');
        comments = [];
        for comms in data:
            comments.append(comms.xpath('string(.)'));
        return comments; 

    def saveToMySQL(self, url, title, description, comments):
        db.execute();

        pass;

    def start(self, total):
        for i in range(1, total):
            try:
                url = self.getUrl(i);
                selector = self.getSelector(bug.getPage(url));
                title = self.getTitle(selector);
                if title == "":
                    break;
                description = self.getDescription(selector);
                comments = self.getComments(selector);
                self.saveToMySQL(url, title, description, comments);
            except Exception as ex:
                print(ex+"["+url+"]");

def start():
    bug = Bugzilla();
    bug.start(99999999999);

if __name__ == '__main__':
    start();