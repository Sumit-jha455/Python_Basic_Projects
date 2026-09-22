# Rock Paper Scissors Game

import random

print("===== ROCK PAPER SCISSORS =====")

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)

user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")

else:
    print("\nYour Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: DRAW")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: YOU WIN!")

    else:
        print("Result: COMPUTER WINS!")