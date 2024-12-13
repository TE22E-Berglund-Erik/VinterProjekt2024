import yfinance as yf

ticker = input("Input symbol (default AAPL): ") or "AAPL"

stock = yf.Ticker(ticker)
history = stock.history(period="1d")["Close"].iloc[-1]

print(f"The latest closing price of {ticker} is: {history}")
