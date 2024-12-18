from Stock import Calc_Stock
from Crypto import Calc_Crypto


class PortfolioManager:
    def __init__(self, currency="USD"):
        self.assets = []
        self.currency = currency

    def add_asset(self, asset):
        self.assets.append(asset)

    def print_portfolio(self):
        if not self.assets:
            print("Your portfolio is empty!")
            return
        total_value = sum(asset.total_value() for asset in self.assets)
        print(f"\nPortfolio ({self.currency}):")
        for asset in self.assets:
            print(asset)
        print(f"Total Value: {total_value} {self.currency}")


def main_menu():
    currency = input(
        "Enter your currency (default USD): ") or "USD"
    portfolio = PortfolioManager(currency)

    while True:
        print("\n1. Add a Stock")
        print("2. Add a Crypto")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter stock ticker: ")
            stock = Calc_Stock(symbol)
            quantity = float(input("Enter quantity: "))
            stock.update_quantity(quantity)
            portfolio.add_asset(stock)
            print(f"Added {symbol} with a value of {stock._price} {currency}!")
        elif choice == "2":
            symbol = input("Enter crypto symbol: ")

            crypto = Calc_Crypto.run_crypto(symbol, portfolio.currency)
            if crypto:
                quantity = float(input("Enter quantity: "))
                crypto.update_quantity(quantity)
                portfolio.add_asset(crypto)
                print(f"Added {symbol} with a value of {crypto._price} {currency}!")

        elif choice == "3":
            portfolio.print_portfolio()

        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main_menu()
