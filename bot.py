import requests
import time
import json
import tweepy
import yfinance as yf
import os.path
from os import path

######################### ADD YOUR VALUES HERE #########################################

#Project Symbol
project_symbol = 'REPLACE-WITH-COLLECTION-SYMBOL'

#Twitter auth details
t_bearer_token='REPLACE'
t_consumer_key='REPLACE'
t_consumer_secret='REPLACE'
t_access_token='REPLACE'
t_access_token_secret='REPLACE'

#If you are granted a higher TPS from MagicEden
TPS = 2

#NFTs called per API request (MAX 500)
nfts_per_call = 500

######################### GLOBAL DEFINITIONS #########################################

#This value is added to the delay in case MagicEden thinks we are cutting too close into their TPS
#If you feel risky lower this value or make it 0
safety_delay = 0.05
delay = 1/TPS + safety_delay

client = tweepy.Client(bearer_token=t_bearer_token,
                       consumer_key=t_consumer_key,
                       consumer_secret=t_consumer_secret,
                       access_token=t_access_token,
                       access_token_secret=t_access_token_secret)

auth = tweepy.OAuth1UserHandler(t_consumer_key, t_consumer_secret, t_access_token, t_access_token_secret)

api = tweepy.API(auth)


######################### FUNCTION DEFINITIONS #########################################

def initCollections():
    limit = nfts_per_call
    url = "http://api-mainnet.magiceden.dev/v2/collections/" + project_symbol + "/activities?offset=0&limit=" + str(limit)
    response = requests.request("GET", url, headers={}, data={}).json()
    return response

def get_json_data(folder):
    f = open("./" + folder + "/" + mint_id + '.json')
    data = json.load(f)
    data = data[folder]
    return data

#Fetches the latest Solana price in USD
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def get_meta_from_mint(mint):
    import requests

    url = "http://api-mainnet.magiceden.dev/v2/tokens/" + mint
    response = requests.request("GET", url, headers={}, data={})

    return response.json()

def send_tweet(api, client, n, meta):
    image = requests.get(meta['image']).content
    with open('./tmp.png', 'wb') as handler:
        handler.write(image)
    mediaID = api.media_upload("tmp.png")
    client.create_tweet(text="BOOM💥 " + meta['name'] +" just sold for " + str(n["price"]) + " SOL ($" + str(round((get_current_price("SOL-USD")*n["price"]), 2)) + " USD)", media_ids=[mediaID.media_id])


######################### DRIVER CODE #########################################


#Getting initial state of sales
activities = initCollections()
last_sale = activities[0]

print("LISTENING FOR " + project_symbol.upper() + " SALES")

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

        if sale['blockTime'] <= last_sale['blockTime'] or count == len(activities):
            break

        if sale['type'] == "buyNow":
            try:
                meta = get_meta_from_mint(sale['tokenMint'])
                time.sleep(delay)
                send_tweet(api, client, sale, meta)
                print("Tweeting: 💥" + meta['name'] + " Sold for " + str(sale['price']))
            except:
                print("ERROR: with NFT that Sold for " + str(sale['price']) + " Not Tweeted")

    last_sale = activities[0]
