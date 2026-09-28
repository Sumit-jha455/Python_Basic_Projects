# Palindrome String Checker

print("===== PALINDROME STRING CHECKER =====")

text = input("Enter a string: ").lower()

# Remove spaces
clean_text = text.replace(" ", "")

reversed_text = clean_text[::-1]

print("\n----- RESULT -----")
print("Original Text:", text)

if clean_text == reversed_text:
    print("Result: It is a Palindrome String.")
else:
    print("Result: It is not a Palindrome String.")