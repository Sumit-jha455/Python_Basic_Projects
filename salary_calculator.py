# Salary Calculator

print("===== SALARY CALCULATOR =====")

basic_salary = float(input("Enter basic salary: "))
hra_percent = float(input("Enter HRA percentage: "))
da_percent = float(input("Enter DA percentage: "))
deduction_percent = float(input("Enter deduction percentage: "))

if basic_salary < 0:
    print("Basic salary cannot be negative.")

elif hra_percent < 0 or da_percent < 0 or deduction_percent < 0:
    print("Percentages cannot be negative.")

else:
    # Calculate allowances
    hra = (basic_salary * hra_percent) / 100
    da = (basic_salary * da_percent) / 100

    # Calculate gross salary
    gross_salary = basic_salary + hra + da

    # Calculate deduction
    deduction = (gross_salary * deduction_percent) / 100

    # Calculate net salary
    net_salary = gross_salary - deduction

    print("\n----- SALARY REPORT -----")
    print("Basic Salary: ₹", round(basic_salary, 2))
    print("HRA: ₹", round(hra, 2))
    print("DA: ₹", round(da, 2))
    print("Gross Salary: ₹", round(gross_salary, 2))
    print("Deduction: ₹", round(deduction, 2))
    print("Net Salary: ₹", round(net_salary, 2))