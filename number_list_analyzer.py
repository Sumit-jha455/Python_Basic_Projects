# Number List Analyzer

print("===== NUMBER LIST ANALYZER =====")

numbers = []

count = int(input("How many numbers do you want to enter? "))

if count <= 0:
    print("Please enter a positive number.")

else:
    for i in range(count):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    total = sum(numbers)
    average = total / len(numbers))
    highest = max(numbers)
    lowest = min(numbers)

    positive = 0
    negative = 0
    zero = 0
    even = 0
    odd = 0

    for number in numbers:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1

        if number.is_integer():
            if int(number) % 2 == 0:
                even += 1
            else:
                odd += 1

    print("\n----- NUMBER ANALYSIS -----")
    print("Numbers:", numbers)
    print("Total:", round(total, 2))
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Positive Numbers:", positive)
    print("Negative Numbers:", negative)
    print("Zeros:", zero)
    print("Even Integers:", even)
    print("Odd Integers:", odd)