from datetime import datetime
from api import get_exchange_rate

def convert(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency.upper(), to_currency.upper())
    
    if rate is None:
        return None, "Rate not found"
    
    result = round(amount * rate, 4)
    return result, None

def save_history(amount, from_cur, to_cur, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {amount} {from_cur} = {result} {to_cur}\n")

if _name_ == "_main_":
    try:
        amount = float(input("Enter amount: "))
        from_cur = input("From currency: ").upper()
        to_cur = input("To currency: ").upper()
        
        result, error = convert(amount, from_cur, to_cur)
        
        if error:
            print(error)
        else:
            print(f"{amount} {from_cur} = {result} {to_cur}")
            save_history(amount, from_cur, to_cur, result)
            print("Saved to history.txt")
    except ValueError:
        print("Invalid amount. Enter a number.")