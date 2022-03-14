# Responsive-Solana-Sales-Bot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;An improvement to [Solana NFT Sales Bot](https://github.com/WilliamAmbrozic/Solana-NFT-Sales-Bot). This bot utilizes MagicEden's ```GET/collections/:symbol/activities``` API call. This bot responds to sales of a given collection in less than a minute while allowing for NFT image uploading and metadata access through MagicEden's API. 

## Contents
- [Setup](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Setup)  
  - [Installing](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Installing-the-Bot)  
  - [Adding Credentials](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Adding-Credentials)
  - [Running](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#Running-the-Bot)  
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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A collection's symbol can be found by going to https://magiceden.io/ and searching for your collections marketplace page (click the search bar). Look at the url and copy the text appearing directly after the last dash following "marketplace" as highlighted above. This text is your collection's symbol, this is needed for the bot to know what collection to tweet out. Paste this value in the project_symbol field found at the beginning of **bot.py** as seen below:
```
project_symbol = 'REPLACE-WITH-COLLECTION-SYMBOL'
```

### 2. Add your Twitter Developer Credentials

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Make a Twitter account and sign up to become a Twitter developer [here](https://developer.twitter.com/).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Make sure your Twitter developer account has elevated access for image uploading [here](https://developer.twitter.com/en/portal/products/elevated).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C. Place your Twitter developer credentials at the top of **bot.py** as seen below:
```
t_bearer_token='REPLACE'
t_consumer_key='REPLACE'
t_consumer_secret='REPLACE'
t_access_token='REPLACE'
t_access_token_secret='REPLACE'
```

## Running the Bot

[[Back to contents]](https://github.com/WilliamAmbrozic/Responsive-Solana-NFT-Sales-Bot#contents)

Run with 
```
python3 bot.py
```
Or with (if you do not want an exit to halt the bot)
```
nohup python3 bot.py &
```

## Find Me

- [williamambrozic.info](https://williamambrozic.info)
- [Twitter](https://twitter.com/WilliamAmbrozic)

## Solana Tip Jar
  * wia.sol 
  * 8vU6RfyFDk9WriVgaJohBxqtE86TLtjAR8cPWjdU6zEN
