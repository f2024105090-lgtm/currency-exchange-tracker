def save_budget(category, amount):
    with open("budget_history.txt", "a") as file:
        file.write(
            f"{category} | ${amount}\n"
        )