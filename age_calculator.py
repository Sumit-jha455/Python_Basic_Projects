# Age Calculator

print("===== AGE CALCULATOR =====")

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

if birth_year > current_year:
    print("Invalid birth year.")
else:
    age = current_year - birth_year

    print("Your approximate age is:", age, "years")