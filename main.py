from flask import Flask, render_template, request
from api import get_exchange_rate
from converter import convert_currency
from history import save_history

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = float(request.form["amount"])

        rate = get_exchange_rate(from_currency, to_currency)

        if rate:
            result = convert_currency(amount, rate)
            save_history(f"{amount} {from_currency} = {result} {to_currency}")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)