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


currency = input("Input currency (default is USD): ") or "USD"
print(f"You selected: {currency}")
value_digits_input = input(
    "Input how many value digits you'd like (default is 2): ")
value_digits = int(value_digits_input) if value_digits_input.strip() else 2


url_multifull = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XRP&tsyms={currency}"
response = requests.get(url_multifull)
data = response.json()

raw_data = (data.get('RAW', {}).get('XRP', {}).get(currency, {}))
_price = round(raw_data.get('PRICE'), value_digits)
_market_cap = round(raw_data.get('MKTCAP'), value_digits)
_current_supply = round(raw_data.get('CIRCULATINGSUPPLY'), value_digits)
_volume24 = round(raw_data.get('VOLUME24HOUR'), value_digits)
_total_supply = round(raw_data.get('SUPPLY'), value_digits)

crypto = Crypto(_price, _market_cap, _current_supply, _volume24, _total_supply)

print(crypto)
