balance = 10000

while True:
    print("\n========================")
    print("ATM SYSTEM")
    print("========================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited.")
            print("Current Balance:", balance)
        else:
            print("Invalid deposit amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn.")
            print("Current Balance:", balance)
        else:
            print("Invalid withdrawal")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")