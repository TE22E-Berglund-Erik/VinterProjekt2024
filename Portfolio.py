class Portfolio_class:
    def __init__(self, price, quantity, market_cap=None):
        self._price = price
        self._quantity = quantity
        self._market_cap = market_cap

    def __str__(self):
        return (f"Portfolio: Price = {self._price}, Quantity = {self._quantity}")
    
    def total_value(self):
        return self._price * self._quantity

    def update_price(self, new_price):
        self._price = new_price

    def update_quantity(self, new_quantity):
        self._quantity = new_quantity