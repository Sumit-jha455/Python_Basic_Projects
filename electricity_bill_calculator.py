# Electricity Bill Calculator

print("===== ELECTRICITY BILL CALCULATOR =====")

units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")

else:
    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

    print("\n----- ELECTRICITY BILL -----")
    print("Units Consumed:", units)
    print("Total Bill: ₹", round(bill, 2))