import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
    
    def convert(self, amount, from_currency, to_currency):
        rates = requests.get(f"{self.api_url}{from_currency}").json().get("rates")
        return amount * rates.get(to_currency)
    
    
if __name__ == "__main__":
    converter = CurrencyConverter()  
    result = converter.convert(100, "USD", "SEK")  
    print(result)


