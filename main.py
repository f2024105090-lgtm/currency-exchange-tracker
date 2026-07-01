from flask import Flask, render_template, request, redirect, session
from auth import save_user, validate_user
from converter import currency_convert
from api import get_weather
from flight import get_flight
from hotel import get_hotel
from package_generator import generate_package

app = Flask(__name__)
app.secret_key = "travelmate_secret"


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        save_user(username, email, password)

        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if validate_user(email, password):
            session["user"] = email
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/currency", methods=["GET", "POST"])
def currency():
    if "user" not in session:
        return redirect("/login")

    result = None
    rate = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        result, rate = currency_convert(amount, from_currency, to_currency)

        with open("currency_history.txt", "a") as file:
            file.write(f"{amount} {from_currency} -> {result} {to_currency}\n")

    return render_template("currency.html", result=result, rate=rate)


@app.route("/weather", methods=["GET", "POST"])
def weather():
    if "user" not in session:
        return redirect("/login")

    weather_data = None

    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(city)

        if weather_data:
            with open("weather_history.txt", "a") as file:
                file.write(f"{city} | {weather_data['temperature']}°C\n")

    return render_template("weather.html", weather_data=weather_data)


@app.route("/flights", methods=["GET", "POST"])
def flights():
    if "user" not in session:
        return redirect("/login")

    flight_data = None

    if request.method == "POST":
        from_city = request.form["from_city"]
        to_city = request.form["to_city"]
        class_type = request.form["class_type"]
        passengers = request.form["passengers"]

        flight_data = get_flight(from_city, to_city, class_type, passengers)

        if flight_data:
            with open("flight_history.txt", "a") as file:
                file.write(f"{from_city} -> {to_city} | {flight_data['airline']}\n")

    return render_template("flights.html", flight_data=flight_data)


@app.route("/hotels", methods=["GET", "POST"])
def hotels():
    if "user" not in session:
        return redirect("/login")

    hotel_data = None

    if request.method == "POST":
        city = request.form["city"]
        hotel_data = get_hotel(city)

        if hotel_data:
            with open("hotel_history.txt", "a") as file:
                file.write(f"{city} | {hotel_data['name']} | ${hotel_data['price']}\n")

    return render_template("hotels.html", hotel_data=hotel_data)


@app.route("/packages", methods=["GET", "POST"])
def packages():
    if "user" not in session:
        return redirect("/login")

    package_data = None

    if request.method == "POST":
        budget = request.form["budget"]
        package_data = generate_package(budget)

        if package_data:
            with open("package_history.txt", "a") as file:
                file.write(
                    f"Budget: {budget} | Destination: {package_data['destination']}\n"
                )

    return render_template("package.html", package_data=package_data)


@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    records = {}

    files = [
        "currency_history.txt",
        "weather_history.txt",
        "flight_history.txt",
        "hotel_history.txt",
        "package_history.txt"
    ]

    for file_name in files:
        try:
            with open(file_name, "r") as file:
                records[file_name] = file.readlines()
        except:
            records[file_name] = []

    return render_template("history.html", records=records)


if __name__ == "__main__":
    app.run(debug=True)