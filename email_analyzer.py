# Email Analyzer

email = input("Enter your email address: ").strip()

print("\n--- Email Analysis ---")

# Basic checks
has_at = "@" in email
has_dot = "." in email
has_space = " " in email

if has_at and has_dot and not has_space:
    print("Email Format: Valid")
else:
    print("Email Format: Invalid")

# Extract username and domain
if "@" in email:
    parts = email.split("@")

    if len(parts) == 2:
        username = parts[0]
        domain = parts[1]

        print("Username:", username)
        print("Domain:", domain)

        # Extract domain extension
        if "." in domain:
            extension = domain.split(".")[-1]
            print("Domain Extension:", extension)

        # Check common email providers
        if domain.lower() == "gmail.com":
            print("Provider: Gmail")
        elif domain.lower() == "outlook.com":
            print("Provider: Outlook")
        elif domain.lower() == "yahoo.com":
            print("Provider: Yahoo")
        else:
            print("Provider: Other")
    else:
        print("Unable to analyze email.")
else:
    print("Invalid email: '@' symbol is missing.")

# Basic information
print("Email Length:", len(email))
print("Contains Space:", "Yes" if has_space else "No")