correct_password = "sumit123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ")

    if pwd == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong password")
            print("Remaining attempts:", attempts)
        else:
            print("Wrong password")
            print("Account locked")