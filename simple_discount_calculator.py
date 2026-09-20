# Simple Discount Calculator

print("===== SIMPLE DISCOUNT CALCULATOR =====")

original_price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

if original_price < 0:
    print("Price cannot be negative.")

elif discount_percent < 0 or discount_percent > 100:
    print("Discount must be between 0% and 100%.")

else:
    discount_amount = (original_price * discount_percent) / 100
    final_price = original_price - discount_amount

    print("\n----- DISCOUNT REPORT -----")
    print("Original Price:", round(original_price, 2))
    print("Discount:", round(discount_percent, 2), "%")
    print("Discount Amount:", round(discount_amount, 2))
    print("Final Price:", round(final_price, 2))