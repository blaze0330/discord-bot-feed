Usage
=====

Use as a normal Python module:

.. code:: python

   from discord_ext import DiscordBot
   feed_url = ""
   discord_webhook_url = ""
   sleep_time = 60*20  # 20 minutes 

   bot = DiscordBot(feed_url, discord_webhook_url, interval=sleep_time)

   bot.send_message_to_discord()


It will fetch rss feed in every 20 minutes and send new items to discord webhook.

- feed_url: The RSS feed URL to monitor
- discord_webhook_url: The Discord webhook URL to send messages to
- sleep_time: The time to sleep between checking the RSS feed for new items(default: 60*20, 20 minutes)


Requirements

- Python 3.6+
- requests