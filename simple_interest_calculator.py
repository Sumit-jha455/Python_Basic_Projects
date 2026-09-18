# Simple Interest Calculator

print("===== SIMPLE INTEREST CALCULATOR =====")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("\n----- Result -----")
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)