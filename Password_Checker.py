"""
Checks a password's length and character variety (digits, uppercase
letters, symbols) and classifies it as Weak, Medium, or Strong.
"""

password = input("Enter a password to check: ").strip()

while len(password) < 8:
    print("Password too short! Must be at least 8 characters.")
    password = input("Enter a password to check: ").strip()

has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_symbol = any(not char.isalnum() for char in password)

variety_count = sum([has_digit, has_upper, has_symbol])

if variety_count <= 1:
    strength = "Weak"
elif variety_count == 2:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Password strength: {strength}")