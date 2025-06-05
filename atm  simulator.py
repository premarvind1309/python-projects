def atm():
    balance = 1000  # starting balance
    pin_code = "1234"  # default PIN

    print("Welcome to Python ATM!")
    entered_pin = input("Please enter your 4-digit PIN: ")

    if entered_pin != pin_code:
        print("❌ Incorrect PIN. Access denied.")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            print(f"💰 Your balance is: ₹{balance}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    balance += amount
                    print(f"✅ ₹{amount} deposited successfully.")
                else:
                    print("❌ Enter a positive amount.")
            except ValueError:
                print("❌ Invalid input.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"✅ ₹{amount} withdrawn successfully.")
                    else:
                        print("❌ Insufficient balance.")
                else:
                    print("❌ Enter a positive amount.")
            except ValueError:
                print("❌ Invalid input.")
        elif choice == "4":
            print("👋 Thank you for using Python ATM. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    atm()
