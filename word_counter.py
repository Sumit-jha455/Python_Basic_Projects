# Word Counter

print("===== WORD COUNTER =====")

text = input("Enter a sentence: ")

words = text.split()

word_count = len(words)

print("\n----- RESULT -----")
print("Text:", text)
print("Total Words:", word_count)