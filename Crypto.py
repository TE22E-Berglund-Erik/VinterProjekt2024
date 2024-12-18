import requests
from Portfolio import Portfolio_class


class Calc_Crypto(Portfolio_class):
    def __init__(self, price, market_cap, current_supply, volume24, total_supply, quantity=0, symbol=None, currency="USD"):
        super().__init__(price, quantity, market_cap)
        self._current_supply = current_supply
        self._volume24 = volume24
        self._total_supply = total_supply
        self._symbol = symbol
        self._currency = currency

    def get_current_supply(self):
        return self.price * self._current_supply

    def __str__(self):
        return (super().__str__() +
                f", Symbol: {self._symbol}, Currency: {self._currency}, Current Supply: {self._current_supply}, "
                f"Volume (24h): {self._volume24}, Total Supply: {self._total_supply}")

    @staticmethod
    def run_crypto(symbol, currency="USD", value_digits=2):
        url_multifull = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={symbol}&tsyms={currency}"
        response = requests.get(url_multifull)
        response.raise_for_status()
        data = response.json()

        raw_data = data.get('RAW', {}).get(symbol, {}).get(currency, {})
        price = round(raw_data.get('PRICE'), value_digits)
        market_cap = round(raw_data.get('MKTCAP'), value_digits)
        current_supply = round(raw_data.get('CIRCULATINGSUPPLY'), value_digits)
        volume24 = round(raw_data.get('VOLUME24HOUR'), value_digits)
        total_supply = round(raw_data.get('SUPPLY'), value_digits)

        return Calc_Crypto(price, market_cap, current_supply, volume24, total_supply, symbol=symbol, currency=currency)
