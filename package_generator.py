def generate_package(budget):
    budget = float(budget)

    if budget < 500:
        destination = "Pakistan"

    elif budget < 1500:
        destination = "Turkey"

    elif budget < 3000:
        destination = "Malaysia"

    else:
        destination = "Japan"

    flight = round(budget * 0.35, 2)
    hotel = round(budget * 0.30, 2)
    food = round(budget * 0.20, 2)
    transport = round(budget * 0.10, 2)
    remaining = round(
        budget - (flight + hotel + food + transport),
        2
    )

    return {
        "destination": destination,
        "flight": flight,
        "hotel": hotel,
        "food": food,
        "transport": transport,
        "remaining": remaining
    }