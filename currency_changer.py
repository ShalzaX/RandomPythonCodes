name = input("Enter your name: ")
print(f"Hello {name}, welcome to the currency converter!")

money = {
    "usd": 1.00,                  # US Dollar
    "eur": 0.85,                  # Euro
    "gbp": 0.72,                  # British Pound
    "chf": 0.92,                  # Swiss Franc
    "cad": 1.25,                  # Canadian Dollar
    "aud": 1.35,                  # Australian Dollar
    "nzd": 1.42,                  # New Zealand Dollar
    "jpy": 110.62,                # Japanese Yen
    "cny": 6.45,                  # Chinese Yuan
    "hkd": 7.78,                  # Hong Kong Dollar
    "sgd": 1.36,                  # Singapore Dollar
    "krw": 1175.50,               # South Korean Won
    "inr": 74.57,                 # Indian Rupee
    "myr": 4.15,                  # Malaysian Ringgit
    "thb": 33.00,                 # Thai Baht
    "sek": 8.65,                  # Swedish Krona
    "nok": 8.90,                  # Norwegian Krone
    "dkk": 6.30,                  # Danish Krone
    "isk": 140.00,                # Icelandic Krona
    "try": 8.50,                  # Turkish Lira
    "ils": 3.25,                  # Israeli Shekel
    "aed": 3.67,                  # UAE Dirham
    "sar": 3.75,                  # Saudi Riyal
    "qar": 3.64,                  # Qatari Riyal
    "omr": 0.39,                  # Omani Rial
    "bhd": 0.38,                  # Bahraini Dinar
    "kwd": 0.30,                  # Kuwaiti Dinar
    "jod": 0.71,                  # Jordanian Dinar
    "egp": 15.70,                 # Egyptian Pound
    "mad": 9.00,                  # Moroccan Dirham
    "dzd": 135.00,                # Algerian Dinar
    "tnd": 2.80,                  # Tunisian Dinar
    "lyd": 4.90,                  # Libyan Dinar
    "sdg": 600.00,                # Sudanese Pound
}


def list_currencies():
    print("Available currencies:")
    for currency in money.keys():
        print(currency.upper(), end=" ")
    print("\n")


def convert_currency(amount, from_currency, to_currency):
    if from_currency not in money or to_currency not in money:
        print("One of the currencies is not supported.")
        return None
    

    usd_value = amount / money[from_currency]
    converted = usd_value * money[to_currency]
    print(f"{amount:,.2f} {from_currency.upper()} = {converted:,.2f} {to_currency.upper()}")
    return converted

def main():
    while True:
        print("\nOptions: 'from' (USD → foreign), 'to' (foreign → USD), 'list' (show currencies), 'convert' (any two currencies)")
        direction = input("Choose an option: ").strip().lower()

        if direction == "from":
            dollars = float(input("Enter amount in dollars: "))
            currency = input("Enter the currency to convert to: ").strip().lower()
            if currency in money:
                print(f"{dollars} USD = {money[currency] * dollars:,.2f} {currency.upper()}")
            else:
                print("Currency not supported.")

        elif direction == "to":
            amount = float(input("Enter amount in foreign currency: "))
            currency = input("Enter the currency you're converting from: ").strip().lower()
            if currency in money:
                print(f"{amount:,.2f} {currency.upper()} = {amount / money[currency]:,.2f} USD")
            else:
                print("Currency not supported.")

        elif direction == "list":
            list_currencies()

        elif direction == "convert":
            amount = float(input("Enter amount: "))
            from_currency = input("Enter currency you want to convert from: ").strip().lower()
            to_currency = input("Enter currency you want to convert to: ").strip().lower()
            convert_currency(amount, from_currency, to_currency)

        else:
            print("Invalid choice. Please type 'from', 'to', 'list', or 'convert'.")

        again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if again not in ["yes", "y", "yeah", "sure", "ok", "okay"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()