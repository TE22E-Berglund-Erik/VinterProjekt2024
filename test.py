import requests

class CurrencyConverter:
    api_url = "https://api.exchangerate-api.com/v4/latest/"
    
    @staticmethod
    def convert(amount, from_currency, to_currency):
        response = requests.get(f"{CurrencyConverter.api_url}{from_currency}")
        rates = response.json()["rates"]
        return amount * rates[to_currency]

if __name__ == "__main__": 
    result = CurrencyConverter.convert(100, "USD", "SEK")  
    print(result)
