import yfinance as yf
from Portfolio import Portfolio


class Stock(Portfolio):
    def __init__(self, ticker, quantity):
        self.ticker = ticker
        

        super().__init__(price=0, market_cap=0, quantity=0)
        self._price, self._market_cap = self.fetch_stock_data()

    def fetch_stock_data(self):
        stock = yf.Ticker(self.ticker)
        stock_info = stock.info

        price = stock_info.get("currentPrice")
        market_cap = stock_info.get("marketCap")

        return price, market_cap

    def get_value(self):
        return self._price * self._quantity

    def __str__(self):
        return (super().__str__() +
                f", Ticker: {self.ticker}, Quantity: {self._quantity}, "
                f"Total Value: {self.get_value()}")
