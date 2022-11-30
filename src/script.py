import requests
from xml.etree.ElementTree import fromstring, ElementTree


class RssFeed(object):
    """ Rss Feed Class
    
    methods:
        __get_feed -> get feed from url
        get_title -> get title of feed
        get_items -> get items of feed
        get_item_by_tag -> get item by tag name from item
    """
    
    def __init__(self, url):
        self.__url = url
        self.__feed = None
        
    @property
    def feed(self):
        if self.__feed is None:
            self.__feed = self._get_feed()
        return self.__feed
    
    def _get_feed(self):
        response = requests.get(self.__url)
        tree = ElementTree(fromstring(response.content))
        return tree

    def get_title(self):
        return self.feed.find('channel/title').text
    
    def get_items(self):
        items = self.feed.findall(f'channel/item')
        total_items = len(items)
        
        return items, total_items
    
    def get_item_by_tag(self, item, tag):
        return item.find(tag).text
