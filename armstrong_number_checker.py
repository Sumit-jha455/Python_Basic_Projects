# Armstrong Number Checker

print("===== ARMSTRONG NUMBER CHECKER =====")

number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a positive number.")

else:
    original_number = number
    digits = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number = number // 10

    if total == original_number:
        print(original_number, "is an Armstrong Number.")
    else:
        print(original_number, "is not an Armstrong Number.")