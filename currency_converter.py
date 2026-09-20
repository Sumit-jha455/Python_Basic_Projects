# Currency Converter
# Fixed / Manual Exchange Rates

print("===== CURRENCY CONVERTER =====")

print("Available currencies:")
print("1. INR - Indian Rupee")
print("2. USD - US Dollar")
print("3. EUR - Euro")
print("4. GBP - British Pound")

currencies = {
    1: "INR",
    2: "USD",
    3: "EUR",
    4: "GBP"
}

# Fixed rates based on INR
rates = {
    "INR": 1.0,
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0
}

from_choice = int(input("Enter source currency (1-4): "))
to_choice = int(input("Enter target currency (1-4): "))
amount = float(input("Enter amount: "))

if from_choice not in currencies or to_choice not in currencies:
    print("Invalid currency choice.")

elif amount < 0:
    print("Amount cannot be negative.")

else:
    from_currency = currencies[from_choice]
    to_currency = currencies[to_choice]

    # Convert source currency to INR
    amount_in_inr = amount * rates[from_currency]

    # Convert INR to target currency
    converted_amount = amount_in_inr / rates[to_currency]

    print("\n----- CONVERSION RESULT -----")
    print("From:", amount, from_currency)
    print("To:", round(converted_amount, 2), to_currency)

    if from_currency == to_currency:
        print("Note: Source and target currencies are the same.")