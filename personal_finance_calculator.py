income = float(input("Enter monthly income: "))
rent = float(input("Enter rent: "))
food = float(input("Enter food expenses: "))
travel = float(input("Enter travel expenses: "))
other = float(input("Enter other expenses: "))

total_expenses = rent + food + travel + other
remaining = income - total_expenses
savings_percentage = (remaining / income) * 100

print("\n--- Personal Finance Summary ---")
print(f"Monthly Income: ₹{income}")
print(f"Total Expenses: ₹{total_expenses}")
print(f"Remaining Money: ₹{remaining}")
print(f"Savings Percentage: {savings_percentage:.2f}%")