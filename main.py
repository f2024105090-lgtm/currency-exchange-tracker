from api import get_exchange_rate
from converter import convert_currency
from history import save_history

def main():
    print("===== LIVE CURRENCY EXCHANGE TRACKER =====")

    while True:
        print("\n1. Convert Currency")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            from_currency = input("From currency (USD): ").upper()
            to_currency = input("To currency (PKR): ").upper()

            try:
                amount = float(input("Amount: "))
            except:
                print("Invalid amount")
                continue

            rate = get_exchange_rate(from_currency, to_currency)

            if rate is None:
                print("Rate not found")
                continue

            result = convert_currency(amount, rate)

            print(f"\n1 {from_currency} = {rate} {to_currency}")
            print(f"{amount} {from_currency} = {result} {to_currency}")

            save_history(f"{amount} {from_currency} = {result} {to_currency}")

        elif choice == "2":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()