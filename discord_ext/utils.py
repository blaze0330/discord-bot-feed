"""
Copyright (c) 2020-2021, PyContributors

Author: Deepak Raj
License: GNU General Public License v3.0
"""

from discord_webhook import DiscordWebhook, DiscordEmbed
import os

from colorama import Fore, Style

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

colors_dict = {
    'red' : Fore.RED,
    'green' : Fore.GREEN,
    'yellow' : Fore.YELLOW,
    'blue' : Fore.BLUE,
    'magenta' : Fore.MAGENTA,
    'cyan' : Fore.CYAN,
    'white' : Fore.WHITE,
    'reset' : Style.RESET_ALL}


def print__(color, text):
    """ Print function to print colored text """
    print(colors_dict[color] + text + colors_dict['reset'])


def _send_message_discord_subfunction(discord_webhook_url: str, 
                            channel_id: str, 
                            bot_version: str,
                            feed_title: str,
                            item_title: str, 
                            item_description: str,
                            item_link: str,
                            item_pubDate: str):
    """ Subfunction to send message to discord using webhook
    
    discord_webhook_url: str -> Edit channel>>Integrations>>Webhooks>>Copy Webhook URL
    channel_id: str -> Discord channel ID, currently not used
    
    bot_version: str -> Bot version from about.py
    
    feed_title: str -> Feed title from feedparser
    
    item_title: str -> Item title from feedparser
    item_description: str -> Item description from feedparser
    item_link: str -> Item link from feedparser
    item_pubDate: str -> Item pubDate from feedparser
    """
    webhook = DiscordWebhook(url=discord_webhook_url, username="{} Bot".format(feed_title))
    embed = DiscordEmbed(title=item_title, description=item_description, color=242424)
    embed.set_url(item_link)
    embed.add_embed_field(name="Published at", value=str(item_pubDate))
    embed.set_author(name='{} Bot v{}'.format(feed_title, bot_version), 
                     url='https://github.com/codeperfectplus', 
                     icon_url='https://github.com/Py-Contributors/Cybel/raw/v2.0.0/images/cybel_icon.jpg')
    embed.set_footer(text='Powered by PyContributors and Python', 
                     icon_url='https://raw.githubusercontent.com/DrakeEntity/project-Image/master/9b2ca712-347a-4987-bac7-a4c3d106ed24_200x200.png')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()


def _read_txt_file(filename):
    """ Read txt file and return list of lines 
    
    Used to read article titles from txt file to avoid duplicate messages on discord
    whenever the bot will send message to discord it will check if the article title is already
    if it is already present in the txt file then it will not send message to discord. otherwise it will send message to discord
    and dump the article title in the txt file
    """
    
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("")
    with open(filename, "r") as f:
        dump_article = f.read().splitlines()

    return dump_article


def _dump_article_title(filename, article_title):
    """ Dump article title in txt file 
    
    Dump article title in txt file to avoid duplicate messages on discord, 
    whenever the bot will send message to discord it will check if the article title is already
    and it will dump the article title in the txt file if it is not already present in the txt file
    """
    with open(filename, "a") as f:
        f.write(article_title + "\n")
