import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if to_currency in data["rates"]:
        rate = data["rates"][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Valutan hittades inte."

# Exempelanvändning
amount = 100
from_currency = "USD"
to_currency = "EUR"

converted = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} är {converted:.2f} {to_currency}")
