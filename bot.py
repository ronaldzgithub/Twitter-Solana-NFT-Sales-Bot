import requests
import time
import json
import tweepy
import yfinance as yf
import os.path
from os import path

######################### GLOBAL DEFINITIONS #########################################

#Fetching config data
conf = open("./config/config.json")
config = json.load(conf)

#List of supported currency
supported_fiat = ["EUR", "USD", "CAD", "JPY", "GPB", "AUD", "CNY", "INR"]

#If you are granted a higher TPS from MagicEden
TPS = 2

#NFTs called per API request (MAX 500)
nfts_per_call = 500

#This value is added to the delay in case MagicEden thinks we are cutting too close into their TPS
#If you feel risky lower this value or make it 0
safety_delay = 0.05
delay = 1/TPS + safety_delay

client = tweepy.Client(bearer_token=config['twtter_credentials']['bearer_token'],
                       consumer_key=config['twtter_credentials']['consumer_key'],
                       consumer_secret=config['twtter_credentials']['consumer_secret'],
                       access_token=config['twtter_credentials']['access_token'],
                       access_token_secret=config['twtter_credentials']['access_token_secret'])

auth = tweepy.OAuth1UserHandler(config['twtter_credentials']['consumer_key'],
                        config['twtter_credentials']['consumer_secret'],
                        config['twtter_credentials']['access_token'],
                        config['twtter_credentials']['access_token_secret'])

api = tweepy.API(auth)


######################### FUNCTION DEFINITIONS #########################################

def initCollections():
    limit = nfts_per_call
    url = "http://api-mainnet.magiceden.dev/v2/collections/" + config['ME_symbol'] + "/activities?offset=0&limit=" + str(limit)
    response = requests.request("GET", url, headers={}, data={}).json()
    return response

#Fetches the latest Solana price in selected currency
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def get_meta_from_mint(mint):
    import requests
    url = "http://api-mainnet.magiceden.dev/v2/tokens/" + mint
    response = requests.request("GET", url, headers={}, data={})
    return response.json()

#Converts tweet text to config text
def convert_tweet(sale_data, meta):
    text = config['tweet_text']
    text = text.replace("[-f]", "$" + str(round((get_current_price("SOL-" + config['fiat_currency'])*sale_data["price"]), 2)) + " " + config['fiat_currency'])
    text = text.replace("[-n]", meta['name'])
    text = text.replace("[-p]", str(sale_data["price"]) + " SOL")
    text = text.replace("[-o]", str(meta["owner"]))
    text = text.replace("[-m]", str(meta["mintAddress"]))
    text = text.replace("[-i]", str(meta["image"]))
    text = text.replace("[-s]", str(sale_data["source"]))
    text = text.replace("[-b]", str(sale_data["blockTime"]))
    return text

def send_tweet(api, client, sale_data, meta):
    image = requests.get(meta['image']).content
    with open('./tmp.png', 'wb') as handler:
        handler.write(image)
    mediaID = api.media_upload("tmp.png")
    client.create_tweet(text=convert_tweet(sale_data, meta), media_ids=[mediaID.media_id])


######################### DRIVER CODE #########################################

#Checking valid currency
if config['fiat_currency'] not in supported_fiat:
    print("INVALID FIAT_CURRENCY: CHECK CONFIG")

#Getting initial state of sales
activities = initCollections()
last_sale = activities[0]

print("LISTENING FOR " + config['ME_symbol'].upper() + " SALES")

while True:
    try:
        activities = initCollections()
        time.sleep(delay)
    except:
        continue

    count = 0

    #Checking for all acticity since last activity
    while True:
        sale = activities[count]
        count += 1

        if sale['signature'] == last_sale['signature'] or count == len(activities):
            break

        if sale['type'] == "buyNow":
            try:
                meta = get_meta_from_mint(sale['tokenMint'])
                time.sleep(delay)
                send_tweet(api, client, sale, meta)
                print("Tweeting: " + convert_tweet(sale, meta))
            except:
                print("ERROR: with NFT that Sold for " + str(sale['price']) + " Not Tweeted")

    last_sale = activities[0]
