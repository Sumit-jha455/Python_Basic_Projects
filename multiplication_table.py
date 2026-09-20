# Multiplication Table Generator

print("===== MULTIPLICATION TABLE GENERATOR =====")

number = int(input("Enter a number: "))

print("\n----- MULTIPLICATION TABLE -----")

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")