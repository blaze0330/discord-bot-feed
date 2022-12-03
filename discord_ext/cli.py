""" 
Copyright (c) 2020-2021, PyContributors

Author: Deepak Raj <deepak008@live.com>
License: GNU General Public License v3.0
"""
import argparse
import sys
sys.path.append('.')
from discord_ext.about import __version__
from discord_ext import DiscordBot

parse = argparse.ArgumentParser(prog="Rss Feed", description="Rss Feed Parser")
parse.add_argument('-f', '--feed-url', help='Url to rss feed', required=True)
parse.add_argument('-d', '--discord-webhook', help='Discord webhook url', required=True)
parse.add_argument('-i', '--interval', help='Interval in seconds', default=600, type=int)

args = parse.parse_args()

bot = DiscordBot(args.feed_url, args.discord_webhook, args.interval)

def main():
    bot.run()


if __name__ == "__main__":
    main()
    