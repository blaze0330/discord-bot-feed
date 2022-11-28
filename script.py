import requests
import pytz
import pandas as pd
from time import sleep
from datetime import datetime, timedelta
from dateutil.parser import parse
from discord_webhook import DiscordWebhook, DiscordEmbed
from xml.etree.ElementTree import fromstring, ElementTree

est_timezone = pytz.timezone('US/Eastern')
est_timenow = est_timezone.localize(parse(str(pd.Timestamp.now())))
est_timenow = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
print("Nasa News Bot is running")
print("Est Time Now", est_timenow)


url = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
# discord_webhook_url = "https://discord.com/api/webhooks/940522536557498368/un_14JP-n7T6haQzIhsDB9Dfj_XjWB_2wYFK6oD-opeC-ZfRhgH29_LSbWnNGnOzGi5B"
discord_webhook_url = "https://discord.com/api/webhooks/940522536557498368/un_14JP-n7T6haQzIhsDB9Dfj_XjWB_2wYFK6oD-opeC-ZfRhgH29_LSbWnNGnOzGi5B"

def create_get_request(url):
    """ create a get request to the url and return the response """
    response = requests.get(url)
    return response


def send_message_to_discord(title, description, link, pubDate, image_url):
    """ Send message to discord """
    webhook = DiscordWebhook(url=discord_webhook_url, username="Nasa News Bot")
    embed = DiscordEmbed(title=title, description=description, color=242424)
    embed.add_embed_field(name="Published at", value=str(pubDate))
    embed.set_url(link)
    embed.set_author(name='Developer(Codeperfectplus)', url='https://github.com/codeperfectplus')
    embed.set_footer(text='Nasa News Bot v1.0')
    # add embed image     
    webhook.add_embed(embed)
    webhook.execute()


def sleep_decorator(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        sleep(60*60*12)  # 12 hours
    return wrapper

# @sleep_decorator
def send_message(response):
    """ 
    main function to iterate over the response and send message to discord
    """ 
    tree = ElementTree(fromstring(response.text))
    root = tree.getroot()

    for item in root.iter('item'):
        title = item.find('title').text
        image_url = item.find('enclosure').attrib['url']
        description = item.find('description').text
        link = item.find('link').text
        pubDate = parse(item.find('pubDate').text)
        
        
        # check if there is any new news published in last 12 hours
        est_timezone  = est_timezone - timedelta(hours=12) 
        if pubDate > est_timezone:
            send_message_to_discord(title, description, link, pubDate, image_url)
            print("Message sent to discord")
                

def main():
    response = create_get_request(url)
    send_message(response)
          
   
if __name__ == '__main__':
    main()
    