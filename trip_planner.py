def save_trip(destination, days, budget):
    with open("trip_history.txt", "a") as file:
        file.write(
            f"{destination} | {days} days | ${budget}\n"
        )