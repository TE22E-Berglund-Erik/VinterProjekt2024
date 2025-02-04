import requests
import pprint

class CurrencyConverter:
   
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/USD")
            response.raise_for_status()
            data = response.json()
            pprint.pprint(data)