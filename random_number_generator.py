# Random Number Generator

import random

print("===== RANDOM NUMBER GENERATOR =====")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start > end:
    print("Starting number must be less than or equal to ending number.")

else:
    random_number = random.randint(start, end)

    print("\n----- RESULT -----")
    print("Range:", start, "to", end)
    print("Random Number:", random_number)