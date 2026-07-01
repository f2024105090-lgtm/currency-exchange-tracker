import requests


def currency_convert(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    rate = data["rates"][to_currency]

    converted = amount * rate

    return converted, rate