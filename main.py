from flask import Flask, render_template, request, redirect
from api import get_exchange_rate, get_all_currencies
from converter import convert_currency
from history import save_history

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    live_rate = None

    currencies = get_all_currencies()

    if not currencies:
        currencies = {"USD": "USD", "PKR": "PKR", "EUR": "EUR"}

    if request.method == "POST":
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")

        try:
            amount = float(request.form.get("amount"))
        except:
            return render_template(
                "index.html",
                result="Invalid amount",
                currencies=currencies
            )

        rate = get_exchange_rate(from_currency, to_currency)

        if rate:
            result = convert_currency(amount, rate)
            live_rate = rate

            save_history(f"{amount} {from_currency} = {result} {to_currency}")
        else:
            result = "Rate not found"

    return render_template(
        "index.html",
        result=result,
        live_rate=live_rate,
        currencies=currencies
    )


@app.route("/history")
def history():
    try:
        with open("history.txt", "r") as f:
            records = f.readlines()
    except:
        records = []

    return render_template("history.html", records=records)


# ⭐ CLEAR HISTORY FEATURE
@app.route("/clear-history")
def clear_history():
    open("history.txt", "w").close()
    return redirect("/history")


if __name__ == "__main__":
    app.run(debug=True)