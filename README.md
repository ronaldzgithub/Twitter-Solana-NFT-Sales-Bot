# Responsive-Solana-Sales-Bot

**Currently testing at:** https://twitter.com/TestSalesBot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This bot allows for **custom tweet text** and **fast response times**. It is an improvement to [Solana NFT Sales Bot](https://github.com/WilliamAmbrozic/Solana-NFT-Sales-Bot). The bot utilizes MagicEden's ```GET/collections/:symbol/activities``` API call, responding to sales in **less than a minute** while allowing for NFT image uploading and metadata access through MagicEden's API. This bot is designed to run on an external server.

**Note: this bot was tested on a [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) and an internet connection** - ($35 USD and under Approx.). All else was free (Twitter access). Usable on any Windows/Unix based server.

## Contents
- [Setup](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Setup)  
  - [Installing](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Installing-the-Bot) 
  - [Adding Credentials](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Adding-Credentials)
  - [Running](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Running-the-Bot)  
- [Config (Customize)](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Config)
- [Credit Not Needed](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Credit-Not-Needed)
- [Find Me](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#find-me)
- [Tip Jar](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Solana-Tip-Jar)

## Setup

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

## Installing the Bot

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

Clone and install Python requirements with
```
git clone https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot.git
cd Responsive-Solana-NFT-Sales-Bot
pip install -r requirements.txt
```

## Adding Credentials

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

### 1. Insert Your NFT MagicEden Collection Symbol 

![shot 1](https://imgur.com/OnbyLbV.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A collection's symbol can be found by going to https://magiceden.io/ and searching for your collection's marketplace page (click the search bar). Look at the url and copy the text appearing directly after the last dash following "marketplace" as highlighted above. This text is your collection's symbol, this is needed for the bot to know what collection to tweet out. Paste this value in the **./config/config.json** attribute called **ME_symbol** as seen [here](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Config).

### 2. Add your Twitter Developer Credentials

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Make a Twitter account and sign up to become a Twitter developer [here](https://developer.twitter.com/).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Make sure your Twitter developer account has elevated access for image uploading [here](https://developer.twitter.com/en/portal/products/elevated).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Place your Twitter developer credentials in **./config/config.json** as seen [here](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Config).

## Running the Bot

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

Run with 
```
python3 bot.py
```
Or recommended with (if you do not want an ssh exit or general exit to halt the bot)
```
nohup python3 bot.py &
```

## Config

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

The config file **./config/config.json** will look something like this:
```
{
  "ME_symbol": "ADD_YOUR_SYMBOL_HERE",
  "twtter_credentials": {
    "bearer_token": "ADD_YOURS_HERE",
    "consumer_key": "ADD_YOURS_HERE",
    "consumer_secret": "ADD_YOURS_HERE",
    "access_token": "ADD_YOURS_HERE",
    "access_token_secret": "ADD_YOURS_HERE"
  },
  "tweet_text": "BOOM💥 [-n] just sold for [-p] ([-f])",
  "fiat_currency": "USD"
}
```

### Optional Attributes
**tweet_text**: You can customize the text that is tweeted out with the NFT image. Tweet text follows this notation (the bot will replace the following syntax with ...):
* [-n]: The NFT name (Ex. SolGod #0001)
* [-f]: The fiat price with respect to the fiat_currency value described below (Ex. $199.19 USD)
* [-p]: The sale price in Solana (Ex. 10 SOL)
* [-o]: The buyers wallet address
* [-m]: The NFT's mint address
* [-i]: The NFT image url
* [-s]: The source of the sale (Ex. magiceden_v2)
* [-b]: The blockTime the transaction occured at (Ex. 21647306453)

For example, 
```
BOOM💥 [-n] just sold for [-p] ([-f])
```
would become
```
BOOM💥 SolGod #001 just sold for 50.24 SOL ($5000.37 USD)
```

**fiat_currency**: The bot currently supports the following currencies: EUR, USD, CAD, JPY, GPB, AUD, CNY, INR. Change this value to change the currency in which Solana is converted if you choose to output fiat price.


## Credit Not Needed

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use of this bot for your project is encouraged. **No credit is needed**. If you find this bot useful and insist on crediting the creator, please add @williamambrozic in the Bot's Twitter bio or simply have the bot follow @williamambrozic on Twitter. Thank you.

## Find Me

- [williamambrozic.info](https://williamambrozic.info)
- [Twitter](https://twitter.com/WilliamAmbrozic)

## Solana Tip Jar
  * wia.sol 
  * 8vU6RfyFDk9WriVgaJohBxqtE86TLtjAR8cPWjdU6zEN
### Bitcoin
  * bc1qa7vkam2w4cgw8njqx976ga5ns8egsq3yzxzlrt
