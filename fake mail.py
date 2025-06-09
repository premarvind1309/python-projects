from validate_email_address import validate_email
import re

def is_valid_format(email):
    # Basic regex to validate format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def detect_fake_email(email):
    if not is_valid_format(email):
        return "❌ Invalid email format. Possibly fake."
    
    is_valid = validate_email(email, check_format=True, check_dns=True, smtp_check=False)
    
    if is_valid:
        return "✅ Email looks real (valid format and domain exists)."
    else:
        return "❌ Email domain not found. Possibly fake."

# Get user input
email = input("Enter an email address to verify: ")
result = detect_fake_email(email)
print(result)
