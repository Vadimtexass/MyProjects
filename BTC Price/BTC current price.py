import requests
from bs4 import BeautifulSoup
import time

# create a function to get price of cryptocurrency


def get_latest_crypto_price(coin):
    url = 'https://www.google.com/search?q=' + coin + 'price'
    # make a request to the website
    htm = requests.get(url)
    # Parse the HTML
    soup = BeautifulSoup(htm.text, 'html.parser')
    # find the current price
    text = soup.find('div', attrs={
        'class': 'BNew iBp4i AP7Wnd'
    }).find({
        'div': 'BNew iBp4i AP7Wnd'
    }).text
    return text


price = get_latest_crypto_price('bitcoin')
print('BITCOIN price : ' + price)