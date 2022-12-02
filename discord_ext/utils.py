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


def send_message_to_discord(discord_webhook_url, feed_title, item_title, item_description, item_link, item_pubDate):
    """ Send message to discord """
    webhook = DiscordWebhook(url=discord_webhook_url, username="{} Bot".format(feed_title))
    embed = DiscordEmbed(title=item_title, description=item_description, color=242424)
    embed.add_embed_field(name="Published at", value=str(item_pubDate))
    embed.set_url(item_link)
    embed.set_author(name='Developer(Codeperfectplus)', url='https://github.com/codeperfectplus')
    embed.set_footer(text='{} Bot v1.0'.format(feed_title))
    webhook.add_embed(embed)
    webhook.execute()


def read_txt_file(filename):
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("")
    with open(filename, "r") as f:
        dump_article = f.read().splitlines()

    return dump_article


def dump_article_title(filename, article_title):
    with open(filename, "a") as f:
        f.write(article_title + "\n")
