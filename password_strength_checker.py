# Password Strength Checker

password = input("Enter your password: ")

score = 0
suggestions = []

# Check password length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# Check uppercase letter
if any(char.isupper() for char in password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

# Check lowercase letter
if any(char.islower() for char in password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

# Check digit
if any(char.isdigit() for char in password):
    score += 1
else:
    suggestions.append("Add at least one number.")

# Check special character
if any(not char.isalnum() for char in password):
    score += 1
else:
    suggestions.append("Add at least one special character.")

# Display result
print("\n--- Password Strength Report ---")

if score == 5:
    print("Password Strength: Very Strong")
elif score >= 4:
    print("Password Strength: Strong")
elif score >= 3:
    print("Password Strength: Moderate")
elif score >= 2:
    print("Password Strength: Weak")
else:
    print("Password Strength: Very Weak")

print("Score:", score, "/ 5")

# Suggestions
if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password meets all basic strength requirements.")