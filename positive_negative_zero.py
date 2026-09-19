# Positive / Negative / Zero Checker

print("===== POSITIVE / NEGATIVE / ZERO CHECKER =====")

number = float(input("Enter a number: "))

if number > 0:
    print("Number:", number)
    print("Result: POSITIVE")

elif number < 0:
    print("Number:", number)
    print("Result: NEGATIVE")

else:
    print("Number:", number)
    print("Result: ZERO")