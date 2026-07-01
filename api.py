import requests


city_coordinates = {
    "lahore": (31.5497, 74.3436),
    "karachi": (24.8607, 67.0011),
    "islamabad": (33.6844, 73.0479),
    "istanbul": (41.0082, 28.9784),
    "ankara": (39.9334, 32.8597),
    "tokyo": (35.6762, 139.6503),
    "paris": (48.8566, 2.3522),
    "london": (51.5072, -0.1276),
    "kuala lumpur": (3.1390, 101.6869),
    "riyadh": (24.7136, 46.6753),
    "new york": (40.7128, -74.0060),
    "dubai": (25.2048, 55.2708)
}


def get_weather(city):
    city = city.lower()

    if city not in city_coordinates:
        return None

    lat, lon = city_coordinates[city]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)
    data = response.json()

    weather = data["current_weather"]

    return {
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "time": weather["time"]
    }