#web-scraping tool
#author: Kevin C

import requests
import tweepy
import time
import schedule
from bs4 import BeautifulSoup
from time import sleep

#twitter dev details
consumer_key = "ENTER CONSUMER KEY"
consumer_secret = "ENTER CONSUMER SECRET"
access_token = "ENTER ACCESS TOKEN"
access_token_secret = "ENTER ACCESS TOKEN SECRET"

#authenticating (OAuth 1.0a)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#post a tweet function
def postTweet():
    #request data from website we're scraping
    URL = "https://coinmarketcap.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    ##################################################################################

    #find crypto_prices and store in a list
    price_results = soup.find_all('div', class_='sc-131di3y-0 cLgOOr')
    crypto_prices = []
    for result in price_results:
        crypto_prices.append(result.text)
    print(crypto_prices)

    #assign crypto_prices to its name
    bitcoin_price = crypto_prices[3]
    ethereum_price = crypto_prices[4]
    xrp_price = crypto_prices[9]
    print("\n\n=----------------------LIVE PRICES----------------------=")
    print("LIVE PRICE: BITCOIN = " + bitcoin_price)
    print("LIVE PRICE: ETHEREUM = " + ethereum_price)
    print("LIVE PRICE: XRP = " + xrp_price)

    ################################################################################

    print("=-------------------------------------------------------=\n")
    localTime = print('The current local time is :', time.ctime())
    print("\n=-------------------------------------------------------=")

    #post tweet
    api.update_status("LIVE! BITCOIN PRICE: " + bitcoin_price)
    api.update_status("LIVE! ETHEREUM PRICE: " + ethereum_price)
    api.update_status("LIVE! XRP PRICE: " + xrp_price)
    print("\n*** TWEET SUCCESSFULLY POSTED ***\n")
    print("=-------------------------------------------------------=")

    #remove all crypto_prices from list
    del crypto_prices[:]
    print(crypto_prices)

postTweet()

#call postTweet every 1 hour at 00 Minutes 00 Seconds.
schedule.every(1).hours.at("00:00").do(postTweet)
while True:
    schedule.run_pending()
    time.sleep(1) 
