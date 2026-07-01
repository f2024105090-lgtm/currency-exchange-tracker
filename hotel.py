import random


def get_hotel(city):
    hotels = [
        "Grand Palace Hotel",
        "Royal Stay",
        "Skyline Resort",
        "Elite Suites",
        "Luxury Inn"
    ]

    return {
        "name": random.choice(hotels),
        "price": random.randint(50, 300),
        "rating": round(random.uniform(3.5, 5.0), 1)
    }