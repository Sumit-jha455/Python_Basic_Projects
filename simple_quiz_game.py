# Simple Quiz Game

print("===== SIMPLE QUIZ GAME =====")

score = 0

print("\nQuestion 1:")
print("What is the capital of India?")
print("A. Mumbai")
print("B. Delhi")
print("C. Kolkata")
print("D. Chennai")

answer = input("Enter your answer: ").lower()

if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B. Delhi.")

print("\nQuestion 2:")
print("Which language is used to create web page structure?")
print("A. Python")
print("B. Java")
print("C. HTML")
print("D. SQL")

answer = input("Enter your answer: ").lower()

if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C. HTML.")

print("\nQuestion 3:")
print("What is 10 + 20?")
print("A. 20")
print("B. 25")
print("C. 30")
print("D. 40")

answer = input("Enter your answer: ").lower()

if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C. 30.")

print("\n===== QUIZ RESULT =====")
print("Your Score:", score, "/ 3")

if score == 3:
    print("Excellent!")
elif score >= 2:
    print("Good Job!")
else:
    print("Keep Practicing!")