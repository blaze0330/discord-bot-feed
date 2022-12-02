import os
import sys
sys.path.append('.')
from time import sleep

from src.api import RssFeed
from src.utils import send_message_to_discord
from src.utils import ROOT_DIR
from src.utils import read_txt_file, dump_article_title


def sleep_decorator(function):
    """ Sleep decorator 
    change sleep time in seconds in sleep(60) 
    
    10 minutes = 600 seconds = 60 * 10
    1 hour = 3600 seconds = 60 * 60
    12 hours = 43200 seconds = 60 * 60 * 12
    """
    def wrapper(*args, **kwargs):
        while True:
            function(*args, **kwargs)
            sleep(60 * 10)  # every 10 minutes
    return wrapper


@sleep_decorator
def main(feed_url, discord_webhook_url):
    rss = RssFeed(feed_url)
    metadata = rss.get_metadata()
    feed_title = metadata['title']  
    print("Starting {} Bot".format(feed_title))
    items = rss.get_items()  # fetch all items from rss feed

    last_txt_file = os.path.join(ROOT_DIR, 'dump.txt')  # dump.txt is the file where we store the last article title
    dump_articles = read_txt_file(last_txt_file)

    for item in items:  # loop through all items 
        item_title = rss.get_item_by_tag(item, 'title')
        item_description = rss.get_item_by_tag(item, 'description')
        item_link = rss.get_item_by_tag(item, 'link')
        item_pubDate = rss.get_item_by_tag(item, 'pubDate')
        
        if item_title not in dump_articles:
            send_message_to_discord(discord_webhook_url, feed_title, item_title, item_description, item_link, item_pubDate)
            dump_article_title(last_txt_file, item_title)  # dump article title to txt file to avoid duplicate message
            
        elif item_title in dump_articles:
            print("Article already sent to discord")
        
        
if __name__ == "__main__":
    feed_url = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
    discord_webhook_url = ""
    main(feed_url, discord_webhook_url)