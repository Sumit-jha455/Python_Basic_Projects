# Area and Perimeter Calculator

import math

print("===== AREA & PERIMETER CALCULATOR =====")
print("1. Rectangle")
print("2. Square")
print("3. Circle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width
    perimeter = 2 * (length + width)

    print("\nArea:", area)
    print("Perimeter:", perimeter)

elif choice == 2:
    side = float(input("Enter side: "))

    area = side ** 2
    perimeter = 4 * side

    print("\nArea:", area)
    print("Perimeter:", perimeter)

elif choice == 3:
    radius = float(input("Enter radius: "))

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print("\nArea:", round(area, 2))
    print("Circumference:", round(circumference, 2))

else:
    print("Invalid choice.")