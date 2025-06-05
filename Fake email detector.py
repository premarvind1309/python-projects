from validate_email import validate_email

def is_fake_email(email):
    # Check syntax and MX records
    is_valid = validate_email(email, check_mx=True)
    return is_valid

email = input("Enter email to check: ")
if is_fake_email(email):
    print(f"{email} is a VALID email address.")
else:
    print(f"{email} is a FAKE or INVALID email address.")
