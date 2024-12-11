import requests
from pprint import pprint


class Crypto:
    def __init__(self, price, market_cap, current_supply, volume24, total_supply):
        self._price = price
        self._market_cap = market_cap
        self._current_supply = current_supply
        self._volume24 = volume24
        self._total_supply = total_supply

    def __str__(self):
        return (f"Price: {self._price}, Market Cap: {self._market_cap}, "
                f"Current Supply: {self._current_supply}, Volume (24h): {self._volume24}, "
                f"Total Supply: {self._total_supply}")


url_multifull = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XRP&tsyms=USD"
response = requests.get(url_multifull)
data = response.json()
pprint(data)

raw_data = data.get('RAW', {}).get('XRP', {}).get('USD', {})

_price = raw_data.get('PRICE')
_market_cap = raw_data.get('MKTCAP')
_current_supply = raw_data.get('CIRCULATINGSUPPLY')
_volume24 = raw_data.get('VOLUME24HOUR')
_total_supply = raw_data.get('SUPPLY')

crypto = Crypto(_price, _market_cap, _current_supply, _volume24, _total_supply)

print(crypto)
