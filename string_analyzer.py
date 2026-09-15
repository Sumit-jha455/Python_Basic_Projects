# String Analyzer

text = input("Enter a string: ")

print("\n--- String Analysis ---")

# Basic information
print("Original String:", text)
print("Length:", len(text))

# Character counts
print("Number of characters:", len(text))
print("Number of spaces:", text.count(" "))
print("Number of vowels:", sum(1 for char in text.lower() if char in "aeiou"))

# Uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# First and last character
if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])

# Check whether string starts/ends with a particular character
print("Starts with a vowel:", text[0].lower() in "aeiou" if text else False)
print("Ends with a vowel:", text[-1].lower() in "aeiou" if text else False)

# Word count
words = text.split()
print("Number of words:", len(words))

# Palindrome check
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")