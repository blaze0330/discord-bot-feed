import requests
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from dateutil.parser import parse
from discord_webhook import DiscordWebhook, DiscordEmbed


url = "https://www.nasa.gov/rss/dyn/breaking_news.rss"
discord_webhook_url = ""


def create_get_request(url):
    """ create a get request to the url and return the response """
    response = requests.get(url)
    return response


def send_message_to_discord(title, description, link, pubDate):
    """ Send message to discord """
    webhook = DiscordWebhook(url=discord_webhook_url, username="Nasa News Bot")
    embed = DiscordEmbed(title=title, description=description, color=242424)
    embed.add_embed_field(name="Published at", value=str(pubDate))
    embed.set_url(link)
    embed.set_author(name='Developer(Codeperfectplus)', url='https://github.com/codeperfectplus')
    embed.set_footer(text='Nasa News Bot v1.0',)    
    webhook.add_embed(embed)
    webhook.execute()

# # not in use right now
# def response_to_dataframe(response):
#     final_output = []
#     Bs_data = BeautifulSoup(response.text, "xml")
#     for item in Bs_data.findAll("item"):
#         nasa_data = {}
#         nasa_data["title"] = item.title.text
#         nasa_data["description"] = item.description.text
#         nasa_data['link'] = item.link.text
#         nasa_data['pubDate'] = parse(item.pubDate.text)
#         nasa_data['identifier'] = parse.find('dc:identifier').text
#         final_output.append(nasa_data)
        
#     df = pd.DataFrame(final_output, columns=["title", "description", "link", "pubDate", 'identifier'])
#     return df

def sleep_decorator(function):
    def wrapper(*args, **kwargs):
        sleep(60)
        function(*args, **kwargs)
    return wrapper

@sleep_decorator
def send_message(response):
    """ 
    main function to iterate over the response and send message to discord
    """
    with open("last_identifier.txt", "r") as f:
        last_indentifier = f.read()
    Bs_data = BeautifulSoup(response.text, "xml")
    for item in Bs_data.findAll("item"):
        title = item.find('title').text
        description = item.find('description').text
        link = item.find('link').text
        pubDate = parse(item.find('pubDate').text)
        identifier = item.find('dc:identifier').text
        
        
        if identifier == last_indentifier:
            break
        elif identifier > last_indentifier:
            last_indentifier = identifier
            send_message_to_discord(title, description, link, pubDate)
            
            print("Last identifier is updated", last_indentifier)
            with open("last_identifier.txt", "w") as fw:
                fw.write(last_indentifier)
                

def main():
    response = create_get_request(url)
    send_message(response)
          
   
if __name__ == '__main__':
    main()
    