import argparse
from api import RssFeed
from discord.about import __version__

parse = argparse.ArgumentParser(prog="Rss Feed", description="Rss Feed Parser")
parse.add_argument("-p", "--path", help="Url/Path to rss feed", required=True)
parse.add_argument("-v", "--version", action="version", version=__version__)
args = parse.parse_args()

def main():
    args = parse.parse_args()
    if args.version:
        print(__version__)


if __name__ == "__main__":
    main()
    