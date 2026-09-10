name = input("Enter student name: ")
age = int(input("Enter age: "))
income = float(input("Enter family income: "))
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance: "))

reasons = []

if age > 25:
    reasons.append("Age is above 25.")
if percentage < 75:
    reasons.append("Percentage below 75%.")
if attendance < 75:
    reasons.append("Attendance below 75%.")
if income > 300000:
    reasons.append("Family income above ₹3,00,000.")

print("\n===============================")
print("SCHOLARSHIP ELIGIBILITY REPORT")
print("===============================")
print(f"Student: {name}")

if len(reasons) == 0:
    print("Status: ELIGIBLE")
    print("Reason: All criteria satisfied.")
else:
    print("Status: NOT ELIGIBLE")
    print("Reasons:")
    for reason in reasons:
        print("-", reason)

print("===============================")