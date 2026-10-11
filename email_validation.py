import re


email = input("Enter your email address: ").strip()

# Keep the validation rules simple and readable for a beginner project.
pattern = r"^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"

if re.fullmatch(pattern, email):
	print("Valid email address")
else:
	print("Invalid email address")
