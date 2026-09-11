p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))

subtotal = p1 + p2 + p3
gst = subtotal * 0.18
final_amount = subtotal + gst
discount = subtotal * 0.10
after_discount = subtotal - discount

print("\n--- Bill Details ---")
print(f"Subtotal: ₹{subtotal}")
print(f"GST (18%): ₹{gst}")
print(f"Final Amount: ₹{final_amount}")
print(f"Amount after 10% Discount: ₹{after_discount}")