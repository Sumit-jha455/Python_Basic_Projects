name = input("Customer Name: ")
amount = float(input("Total Purchase Amount: "))
member = input("Membership (Y/N): ").strip().upper()

if member == "Y":
    if amount >= 10000:
        discount_percent = 20
    elif amount >= 5000:
        discount_percent = 15
    elif amount >= 2000:
        discount_percent = 10
    else:
        discount_percent = 5
else:
    if amount >= 10000:
        discount_percent = 10
    elif amount >= 5000:
        discount_percent = 7
    elif amount >= 2000:
        discount_percent = 5
    else:
        discount_percent = 0

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount

print(f"Customer: {name}")
print(f"Purchase Amount: ₹{amount}")
print(f"Discount: {discount_percent}%")
print(f"Discount Amount: ₹{discount_amount}")
print(f"Final Amount: ₹{final_amount}")