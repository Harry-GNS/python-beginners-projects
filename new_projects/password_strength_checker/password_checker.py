# Password Strength Checker

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) < 8:
    print("Weak password: Use at least 8 characters.")
elif has_upper and has_lower and has_digit and has_special:
    print("Strong password!")
else:
    print("Medium password: Add uppercase, lowercase, number, and special character.")