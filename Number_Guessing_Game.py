# Number Guessing Game

import random

print("===== NUMBER GUESSING GAME =====")

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")

    elif guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Number:", secret_number)
        print("Attempts:", attempts)
        break