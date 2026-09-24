# Factorial Calculator

print("===== FACTORIAL CALCULATOR =====")

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    print("\nNumber:", number)
    print("Factorial:", factorial)