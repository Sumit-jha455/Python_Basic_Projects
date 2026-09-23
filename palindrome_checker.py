# Palindrome Checker

print("===== PALINDROME CHECKER =====")

text = input("Enter a word or number: ").lower()

reversed_text = text[::-1]

print("\nOriginal:", text)
print("Reversed:", reversed_text)

if text == reversed_text:
    print("Result: It is a Palindrome.")
else:
    print("Result: It is not a Palindrome.")