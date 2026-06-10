import requests

def get_exchange_rate(from_currency, to_currency):
    try:
        url = f"https://api.fxratesapi.com/latest?base={from_currency}&symbols={to_currency}"
        response = requests.get(url, timeout=5)
        data = response.json()

        return data["rates"][to_currency]

    except:
        return None