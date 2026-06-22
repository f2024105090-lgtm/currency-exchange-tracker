from flask import Flask, render_template, request
from api import get_exchange_rate
from converter import convert_currency
from history import save_history

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    live_rate = None
    from_currency = None
    to_currency = None

    if request.method == "POST":
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()

        try:
            amount = float(request.form["amount"])
        except ValueError:
            return render_template("index.html", result="Invalid amount")

        rate = get_exchange_rate(from_currency, to_currency)

        if rate is None:
            result = "Rate not found"
        else:
            live_rate = rate
            result = convert_currency(amount, rate)

            record = f"{amount} {from_currency} = {result} {to_currency}"
            save_history(record)

    return render_template(
        "index.html",
        result=result,
        live_rate=live_rate,
        from_currency=from_currency,
        to_currency=to_currency
    )


@app.route("/history")
def history():
    try:
        with open("history.txt", "r") as file:
            records = file.readlines()
    except FileNotFoundError:
        records = []

    return render_template("history.html", records=records)


if __name__ == "__main__":
    app.run(debug=True)