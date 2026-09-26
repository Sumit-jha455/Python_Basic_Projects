# Duplicate Character Finder

print("===== DUPLICATE CHARACTER FINDER =====")

text = input("Enter a string: ").lower()

frequency = {}

for character in text:
    if character != " ":
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

print("\n----- DUPLICATE CHARACTERS -----")

found = False

for character, count in frequency.items():
    if count > 1:
        print(character, ":", count, "times")
        found = True

if not found:
    print("No duplicate characters found.")