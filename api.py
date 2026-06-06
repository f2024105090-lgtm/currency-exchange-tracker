import requests

def get_exchange_rate(from_currency, to_currency):
    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url, timeout=10)
        data = response.json()

        if data["result"] == "success":
            rates = data["rates"]
            return rates.get(to_currency, None)

        return None

    except Exception as e:
        print("ERROR:", e)
        return None


print(get_exchange_rate("USD", "PKR"))