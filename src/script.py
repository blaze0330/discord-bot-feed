import os
import requests
from xml.etree.ElementTree import fromstring, ElementTree


class ErrorHandling(Exception):
    pass


class RssFeed(object):
    """ Rss Feed Class

    methods:
            __get_feed -> get feed from url
            get_title -> get title of feed
            get_items -> get items of feed
            get_item_by_tag -> get item by tag name from item
    """

    def __init__(self, path=None):
        self.__path = path
        self.__feed = None

    def __str__(self):
        return f'RssFeed(url={self.__path})'

    @property
    def feed(self):
        if self.__feed is None:
            self.__feed = self.__get_feed()
        return self.__feed

    def __feed_from_url(self, url):
        """
        get feed from url
        """
        response = requests.get(url)
        tree = ElementTree(fromstring(response.content))
        return tree

    def __feed_from_file(self, filename):
        """ get feed from file """
        return ElementTree(file=filename)

    def __get_feed(self):
        """ get feed from url or file """
        if self.__path.startswith('http'):
            return self.__feed_from_url(self.__path)
        elif self.__path.endswith('.xml'):
            if os.path.exists(self.__path):
                return self.__feed_from_file(self.__path)
            raise ErrorHandling(f'File {self.__path} not found')
        else:
            raise ErrorHandling('Invalid path or url provided for feed')

    def get_metadata(self):
        """ get metadata of feed """
        metadata = {}
        metadata['title'] = self.feed.find('channel/title').text
        metadata['link'] = self.feed.find('channel/link').text
        metadata['description'] = self.feed.find('channel/description').text
        metadata['language'] = self.feed.find('channel/language').text
        return metadata

    def get_items(self):
        """ get items of feed """
        items = self.feed.findall(f'channel/item')
        return items

    def get_item_by_tag(self, item, tag):
        """ get item by tag name from item """
        return item.find(tag).text

    def save_feed(self, filename):
        """ save feed to file """
        self.feed.write(filename)
