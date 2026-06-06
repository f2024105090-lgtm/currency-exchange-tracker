def save_history(record):
    with open("history.txt", "a") as file:
        file.write(record + "\n")