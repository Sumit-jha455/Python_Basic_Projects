name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
hra_percent = float(input("Enter HRA percentage: "))
da_percent = float(input("Enter DA percentage: "))
tax_percent = float(input("Enter tax percentage: "))

hra = basic * hra_percent / 100
da = basic * da_percent / 100
gross = basic + hra + da
tax = gross * tax_percent / 100
net = gross - tax

print("\n--- Employee Salary Details ---")
print(f"Employee Name: {name}")
print(f"Basic Salary: ₹{basic}")
print(f"HRA: ₹{hra}")
print(f"DA: ₹{da}")
print(f"Gross Salary: ₹{gross}")
print(f"Tax: ₹{tax}")
print(f"Net Salary: ₹{net}")