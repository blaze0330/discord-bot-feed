<h1 align="center">RSS Feed</h1>
<p align="center">Discord bot for automating RSS feed updates.</p>

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

Check out the [documentation](#) for more information on how to use RSS Feed.


```python
from discord_ext import DiscordBot
feed_url = ""
discord_webhook_url = ""
sleep_time = 60*20  # 20 minutes 
bot = DiscordBot(discord_webhook_url, feed_url, sleep_time=sleep_time)
bot.send_message_to_discord()
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

- [GNU General Public License v3.0](/LICENSE)

## Authors

- [Deepak Raj](https://github.com/codePerfectPlus)
