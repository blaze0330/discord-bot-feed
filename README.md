<h1 align="center">RSS Feed</h1>
<p>Simple Python Library for Automating RSS Feed</p>

## Installation

```bash
pip install <coming soon>
```

## Features

- [x] Get RSS Feed from URL/File
- [x] Get Metadata from RSS Feed
- [x] Get Items from RSS Feed

## Usage

Check out the [documentation](#) for more information on how to use RSS Feed.


```python
from discord import DiscordBot
feed_url = ""
discord_webhook_url = ""
sleep_time = 60*20  # 20 minutes 
bot = DiscordBot(discord_webhook_url, feed_url, sleep_time=sleep_time)
bot.send_message_to_discord()
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

