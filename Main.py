from Portfolio import Portfolio_class
from currency_converter import CurrencyConverter


if __name__ == "__main__":
    converter = CurrencyConverter("USD")
    result = converter.convert(100, "EUR")
    print(result)
