class Portfolio_class:
    def __init__(self, price=0, quantity=0, market_cap=None, currency="USD"):
        self._price = price
        self._quantity = quantity
        self._market_cap = market_cap
        self._currency = currency
        self.assets = []

    def __str__(self):
        return f"Portfolio: Price = {self._price}, Quantity = {self._quantity}"

    def total_value(self):
        return self._price * self._quantity

    def update_price(self, new_price):
        self._price = new_price

    def update_quantity(self, new_quantity):
        self._quantity = new_quantity

    def add_asset(self, asset):
        self.assets.append(asset)

    def print_portfolio(self):
        if not self.assets:
            print("\nYour portfolio is empty!")
            return
        total_value = sum(asset.total_value() for asset in self.assets)
        print(f"\nPortfolio ({self._currency}):")
        for asset in self.assets:
            print(asset)
        print(f"Total Value: {round((total_value),2)} {self._currency}")

    def manage_portfolio(self):
        self._currency = input("Enter your currency (default USD): ") or "USD"

        while True:
            print("\n1. Add a Stock")
            print("2. Add a Crypto")
            print("3. View Portfolio")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                from Stock import Calc_Stock
                symbol = input("Enter stock ticker: ")
                stock = Calc_Stock(symbol)
                print(f"{stock._name} are currently going for {stock._price} {self._currency}")
                quantity = float(input("Enter quantity: "))
                stock.update_quantity(quantity)
                self.add_asset(stock)
                print(f"Added {symbol.upper()} with a total value of {stock._price*quantity} {self._currency}!")

            elif choice == "2":
                from Crypto import Calc_Crypto
                symbol = input("Enter crypto symbol: ")
                crypto = Calc_Crypto.run_crypto(symbol, self._currency)
                if crypto:
                    print(f"{symbol} are currently going for {crypto._price} ")
                    quantity = float(input("Enter quantity: "))
                    crypto.update_quantity(quantity)
                    self.add_asset(crypto)
                    print(f"Added {symbol.upper()} with a total value of {crypto._price*quantity} {self._currency}!")

            elif choice == "3":
                self.print_portfolio()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option, try again.")
