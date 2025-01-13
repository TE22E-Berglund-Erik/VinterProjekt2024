import yfinance as yf
from Portfolio import Portfolio_class


class Calc_Stock(Portfolio_class):
    def __init__(self, ticker):
        self.ticker = ticker
        
        super().__init__(price=0, market_cap=0, quantity=0)
        self._price, self._market_cap, self._name = self.fetch_stock_data()

    def fetch_stock_data(self):
        stock = yf.Ticker(self.ticker)
        stock_info = stock.info

        price = stock_info.get("currentPrice")
        market_cap = stock_info.get("marketCap")
        name = stock_info.get("longName") 

        return price, market_cap, name

    def get_value(self):
        return self._price * self._quantity

    def __str__(self):
        return (super().__str__() +
                f", Name: {self._name}, Ticker: {self.ticker}, Quantity: {self._quantity}, "
                f"Total Value: {self.get_value()}")
