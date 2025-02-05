import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

    @staticmethod
    def convert(amount, from_currency, to_currency):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        rates = requests.get(api_url).json().get("rates")
        return amount * rates.get(to_currency)