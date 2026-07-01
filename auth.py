import json
import os


def load_users():
    if not os.path.exists("users.json"):
        return []

    with open("users.json", "r") as file:
        return json.load(file)


def save_user(username, email, password):
    users = load_users()

    users.append({
        "username": username,
        "email": email,
        "password": password
    })

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def validate_user(email, password):
    users = load_users()

    for user in users:
        if user["email"] == email and user["password"] == password:
            return True

    return False