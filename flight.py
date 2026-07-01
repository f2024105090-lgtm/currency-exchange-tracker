import requests


API_KEY = "1931e461196cfbe635f6811d41c02be7"


def get_flight(from_city, to_city, class_type, passengers):
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&dep_iata={from_city}&arr_iata={to_city}"

    response = requests.get(url)
    data = response.json()

    if "data" not in data or len(data["data"]) == 0:
        return None

    flight = data["data"][0]

    base_price = 300

    if class_type == "Business":
        base_price += 250
    elif class_type == "First Class":
        base_price += 500

    total_price = base_price * int(passengers)

    return {
        "airline": flight["airline"]["name"],
        "price": total_price,
        "duration": "Live duration unavailable"
    }