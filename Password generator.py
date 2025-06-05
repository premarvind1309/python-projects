import random
import string

def generate_password(length):
    if length < 4:
        return "❌ Password too short. Minimum length is 4."

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    # Ensure at least one of each type is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# --- Run Program ---
try:
    length = int(input("Enter desired password length (min 4): "))
    pwd = generate_password(length)
    print("\n🔐 Your secure password:\n", pwd)
except ValueError:
    print("❌ Please enter a valid number.")
