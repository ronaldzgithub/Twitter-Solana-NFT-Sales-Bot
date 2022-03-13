import requests
import time
import json
import tweepy
import yfinance as yf
import os.path
from os import path
import copy

######################### GLOBAL DEFINITIONS #########################################

#Project mint id
mint_id = ""

#Twitter auth details
t_bearer_token=''
t_consumer_key=''
t_consumer_secret=''
t_access_token=''
t_access_token_secret=''

#Capped under the magiceden max call rate for default access
TPS = 2
#This value is added to the delay in case MagicEden thinks we are cutting too close into their TPS
#If you feel risky lower this value or make it 0
safety_delay = 0.05
delay = 1/TPS + safety_delay

#NFTs called per API request (MAX 500)
nfts_per_call = 500

client = tweepy.Client(bearer_token=t_bearer_token,
                       consumer_key=t_consumer_key,
                       consumer_secret=t_consumer_secret,
                       access_token=t_access_token,
                       access_token_secret=t_access_token_secret)

auth = tweepy.OAuth1UserHandler(t_consumer_key, t_consumer_secret, t_access_token, t_access_token_secret)

api = tweepy.API(auth)

project_name = "drippies"
mint_id = "6ALSbyHmEoAipobMGG1yNQsgFEoYxyiBZVAy5spMPuPB"

######################### FUNCTION DEFINITIONS #########################################

def initCollections():
    collections = []
    offset = 0
    limit = nfts_per_call
    while True:
        url = "http://api-mainnet.magiceden.dev/v2/collections/" + project_name + "/activities?offset=" + str(offset) + "&limit=" + str(limit)
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()
        offset += nfts_per_call
        if response == []:
            break;
        #print(len(response))
        for res in response:
            collections.append(res)
        time.sleep(delay)

    return collections

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
'''
def get_meta_from_mint(meta, mint_addr):
    for m in meta:
        if m[]
'''

def send_tweet(api, client, n):
    #print("SALE:", meta[m]['name'] ,"just sold for " + str(n["price"]) + " SOL")
    #image = requests.get(meta[m]['image']).content
    #with open('./save.png', 'wb') as handler:
    #    handler.write(image)
    #mediaID = api.media_upload("save.png")
    client.create_tweet(text="BOOM💥 " + "Drippies" +" just sold for " + str(n["price"]) + " SOL ($" + str(round((get_current_price("SOL-USD")*n["price"]), 2)) + " USD)")


######################### DRIVER CODE #########################################

# Opening JSON file
meta = get_json_data('metadata');

#Getting initial state of sales
activities = initCollections()
last_sale = activities[0]

print("LISTENING")

while True:

    activities = initCollections()

    count = 0
    #Checking for all acticity since last activity
    while True:
        sale = activities[count]
        count += 1

        if sale['blockTime'] <= last_sale['blockTime'] or count == len(activities):
            break

        if sale['type'] == "buyNow":
            send_tweet(api, client, sale)
            print("💥NFT Sold for " + str(sale['price']))

        #sale = activities[0]
        #print(sale)
        #print("💥NFT Sold for " + str(sale['price']))

    last_sale = activities[0]
