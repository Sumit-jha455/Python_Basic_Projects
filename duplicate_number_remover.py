# Duplicate Number Remover

print("===== DUPLICATE NUMBER REMOVER =====")

numbers = []

count = int(input("How many numbers do you want to enter? "))

if count <= 0:
    print("Please enter a positive number.")

else:
    for i in range(count):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("\n----- RESULT -----")
    print("Original List:", numbers)
    print("List Without Duplicates:", unique_numbers)