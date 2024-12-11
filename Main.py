
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
