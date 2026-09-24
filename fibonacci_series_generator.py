# Fibonacci Series Generator

print("===== FIBONACCI SERIES GENERATOR =====")

terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")

else:
    first = 0
    second = 1

    print("\nFibonacci Series:")

    for i in range(terms):
        print(first, end=" ")

        next_number = first + second
        first = second
        second = next_number

    print()