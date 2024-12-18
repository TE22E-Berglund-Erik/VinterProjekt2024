
class Portfolio:
    def __init__(self, price, quantity,market_cap=None):
        self._price = price
        self._quantity = quantity
        self._market_cap = market_cap
        