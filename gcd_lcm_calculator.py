# GCD & LCM Calculator

print("===== GCD & LCM CALCULATOR =====")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 <= 0 or num2 <= 0:
    print("Please enter positive numbers.")

else:
    # Calculate GCD using Euclidean algorithm
    a = num1
    b = num2

    while b != 0:
        a, b = b, a % b

    gcd = a

    # Calculate LCM
    lcm = (num1 * num2) // gcd

    print("\n----- RESULT -----")
    print("First Number:", num1)
    print("Second Number:", num2)
    print("GCD:", gcd)
    print("LCM:", lcm)