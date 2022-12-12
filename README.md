<h1 align="center">RSS Feed</h1>
<p align="center">Discord bot for automating RSS feed updates.</p>

<p align="center">
    <a href="https://twitter.com/pycontributors"><img src="https://img.shields.io/twitter/follow/pycontributors?style=social" alt="Twitter" /></a>
    <a href="https://github.com/codeperfectplus?tab=followers"><img src="https://img.shields.io/github/followers/codeperfectplus.svg?style=social&label=Follow&maxAge=2592000"/></a>
</p>

## Installation

```bash
pip install discord-feed-bot
```

## Features

- [x] Get RSS Feed from URL/File
- [x] Get Metadata from RSS Feed
- [x] Get Items from RSS Feed
- [x] Auto Update RSS Feed on Discord 

## Usage

Check out the [documentation](https://discord-feed-bot.readthedocs.io/en/latest/) for more information on how to use RSS Feed.


```python
from discord_ext import DiscordBot
feed_url = ""
discord_webhook_url = ""
sleep_time = 60 * 20  # 20 minutes 
bot = DiscordBot(feed_url, discord_webhook_url, interval=sleep_time)
bot.send_message_to_discord()
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

- [GNU General Public License v3.0](https://github.com/Py-Contributors/discord-feed-bot/LICENSE)

## Authors

- [Deepak Raj](https://github.com/codePerfectPlus)
