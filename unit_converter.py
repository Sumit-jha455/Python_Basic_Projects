# Unit Converter

print("===== UNIT CONVERTER =====")
print("1. Length")
print("2. Weight")
print("3. Temperature")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")

    option = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if option == 1:
        result = value * 0.621371
        print("Result:", round(result, 2), "miles")

    elif option == 2:
        result = value * 1.60934
        print("Result:", round(result, 2), "kilometers")

    elif option == 3:
        result = value * 3.28084
        print("Result:", round(result, 2), "feet")

    elif option == 4:
        result = value * 0.3048
        print("Result:", round(result, 2), "meters")

    else:
        print("Invalid choice.")

elif choice == 2:
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    option = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if option == 1:
        result = value * 2.20462
        print("Result:", round(result, 2), "pounds")

    elif option == 2:
        result = value * 0.453592
        print("Result:", round(result, 2), "kilograms")

    else:
        print("Invalid choice.")

elif choice == 3:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    option = int(input("Enter your choice: "))
    value = float(input("Enter temperature: "))

    if option == 1:
        result = (value * 9 / 5) + 32
        print("Result:", round(result, 2), "°F")

    elif option == 2:
        result = (value - 32) * 5 / 9
        print("Result:", round(result, 2), "°C")

    else:
        print("Invalid choice.")

else:
    print("Invalid choice.")