# Cryptocurrency Webscraper + Automated Twitter bot

_Webscrape cryptocurrency data which is stored and used to Tweet a LIVE price of specific cryptocurrencies on a fixed hourly schedule._

----

Strictly written with **Python** with the implementation of the following libraries, packages and modules: 
  * [BeautifulSoup](https://pypi.org/project/beautifulsoup4/): used to gather data from HTML and XML pages.
  * [Requests](https://pypi.org/project/requests/): used to send HTTP requests.
  * [Tweepy](https://docs.tweepy.org/en/stable/): library used to easily access the twitter API.
  * [Time](https://docs.python.org/3/library/time.html): used to access local time.
  * [Schedule](https://schedule.readthedocs.io/en/stable/): used to schedule a function (postTweet).

----

 #### How to Install and Run:
  1. Download and extract GitHub files.
  2. Open extracted folder in your preferred IDE.
  3. Install **all** resources above.

 #### How it Works:
  1. Replace "ENTER CONSUMER/ACCESS KEY HERE" with your unique keys (Accessible on your [Developer Twitter](http://developer.twitter.com/) account).
  2. We authenticate our Twitter account using [Tweepy](https://docs.tweepy.org/en/stable/).
  3. Using [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) and a simple for loop we are able to iterate through the [CoinMarketCap](coinmarketcap.com) class which holds a crypocurrencies price and store it in a list (crypto_prices).
  4. Assign the position of a cryptocurrency from the list to its variable. (e.g. bitcoin_price = crypto_prices[3])
  5. Using [Tweepy](https://docs.tweepy.org/en/stable/), we call update_status(bitcoin_price) to post a tweet of the LIVE price of a cryptocurrency.
  6. Finally, we use [Schedule](https://schedule.readthedocs.io/en/stable/) to call our postTweet() function every hour at 00 minutes 00 seconds.

----
