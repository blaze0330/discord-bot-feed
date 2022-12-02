'''
Copyright (c) 2020-2021
	- PyContributors <pycontributors@gmail.com>
	- Deepak Raj <deepak008@live.com>

License: GNU General Public License v3.0
'''
import os
import requests
from time import sleep
from urllib.parse import urlparse
from xml.etree.ElementTree import fromstring
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import ParseError

from discord_ext.utils import print__
from discord_ext.utils import read_txt_file
from discord_ext.utils import dump_article_title
from discord_ext.utils import send_message_to_discord

expand_usr = os.path.expanduser('~')


class ErrorHandling(Exception):
	pass


class RssFeed(object):
	''' Rss Feed Class

	methods:
		__get_feed -> get feed from url
		get_title -> get title of feed
		get_items -> get items of feed
		get_item_by_tag -> get item by tag name from item
	'''
	def __init__(self, feed_url=None):
		self.__feed_url = feed_url

	def __str__(self):
		return f'RssFeed(url={self.__feed_url})'

	@property
	def feed(self):
		return self.__get_feed()

	def __get_request(self, url):
		try:
			data = requests.get(url)
			print(f'Fetching URL -> {data.status_code}')
		except Exception as e:
			raise ErrorHandling(f'Error while getting data from {url}: {e}')
		return data

	def __feed_from_url(self, url):
		''' get feed from url '''
		response = self.__get_request(url)
		try:
			tree = ElementTree(fromstring(response.content))
		except (ParseError) as e:
			raise ErrorHandling(f'Error while parsing feed from {url}: {e}')
		return tree

	def __feed_from_file(self, filename):
		''' get feed from file '''
		try:
			tree = ElementTree(file=filename)
		except (ParseError) as e:
			raise ErrorHandling(f'Error while parsing feed from {filename}: {e}')
		return tree

	def __get_feed(self):
		''' get feed from url or file '''
		if urlparse(self.__feed_url)[0] in ('http', 'https'):
			return self.__feed_from_url(self.__feed_url)

		elif self.__feed_url.endswith('.xml'):
			if os.path.exists(self.__feed_url):
				return self.__feed_from_file(self.__feed_url)
			raise FileNotFoundError(f'File {self.__feed_url} not found')
		else:
			raise NotImplementedError('Invalid path or url provided for feed')

	def get_metadata(self):
		''' get metadata of feed '''
		metadata = {}
		cache = self.feed
		metadata['title'] = cache.find('channel/title').text
		metadata['link'] = cache.find('channel/link').text
		metadata['description'] = cache.find('channel/description').text
		metadata['language'] = cache.find('channel/language').text

		return metadata

	def get_items(self):
		''' get items of feed '''
		items = self.feed.findall(f'channel/item')
		return items

	def get_item_by_tag(self, item, tag):
		''' get item by tag name from item '''
		return item.find(tag).text

	def save_feed(self, filename):
		''' save feed to file '''
		self.feed.write(filename)


class DiscordBot(RssFeed):
	''' DiscordBot Class

	methods:
		send_message_to_discord -> send message to discord
		save_feed -> save feed to file
		get_metadata -> get metadata from feed
	'''
	def __init__(self, feed_url=None, discord_webhook_url=None, channel_id=None, interval=10):
		super().__init__(feed_url)
		self.__discord_webhook_url = discord_webhook_url
		self.__channel_id = channel_id
		self.__interval = interval
		self.__dump_article_file = os.path.join(expand_usr, 'dump.txt')
 
	def get_metadata(self):
		return super().get_metadata()

	def save_feed(self, filename):
		return super().save_feed(filename)

	def send_message_to_discord(self):
		metadata = super().get_metadata()
		feed_title = metadata['title']
		
		print__('green', 'Starting {} Bot'.format(feed_title))
		print__('red', 'Running Bot... Press Ctrl+C to stop')
		print('Checking for new articles every {} seconds'.format(self.__interval))

		while True:
			items = super().get_items()[::-1]  # fetch all items from rss feed
			dump_articles = read_txt_file(self.__dump_article_file)  # read dump.txt file

			for item in items:  # loop through all items
				item_title = super().get_item_by_tag(item, 'title')
				item_description = super().get_item_by_tag(item, 'description')
				item_link = super().get_item_by_tag(item, 'link')
				item_pubDate = super().get_item_by_tag(item, 'pubDate')

				if item_title not in dump_articles:
					send_message_to_discord(self.__discord_webhook_url, feed_title, item_title, item_description, item_link, item_pubDate)
					dump_article_title(self.__dump_article_file, item_title)  # dump article title to txt file to avoid duplicate message
					print('Sending message to discord')
			sleep(self.__interval)
