import requests


def get_exchange_rate(from_currency, to_currency):
    try:
        url = f"https://api.fxratesapi.com/latest?base={from_currency}&symbols={to_currency}"
        data = requests.get(url).json()

        return data["rates"].get(to_currency)

    except:
        return None


def get_all_currencies():
    try:
        # FIXED RELIABLE SOURCE
        url = "https://open.er-api.com/v6/latest/USD"
        data = requests.get(url).json()

        # returns all currencies in "rates"
        rates = data.get("rates", {})

        # convert to dropdown format
        currencies = {}
        for code in rates.keys():
            currencies[code] = code

        return currencies

    except:
        return {"USD": "USD", "PKR": "PKR", "EUR": "EUR"}