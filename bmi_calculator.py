# BMI Calculator

print("===== BMI CALCULATOR =====")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if height <= 0 or weight <= 0:
    print("Invalid input. Weight and height must be greater than 0.")

else:
    bmi = weight / (height ** 2)

    print("\n----- BMI REPORT -----")
    print("Weight:", weight, "kg")
    print("Height:", height, "m")
    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    print("Category:", category)