balance = 0.0

def add_balance():
    global balance
    try:
        amount = float(input("Enter amount to add: "))
        if amount <= 0:
            raise ValueError("Amount must be positive")
        balance += amount
        print("Balance added successfully")
    except ValueError as e:
        print("Error:", e)

def make_payment():
    global balance
    try:
        amount = float(input("Enter payment amount: "))
        if amount <= 0:
            raise ValueError("Invalid amount")
        if amount > balance:
            raise ValueError("Insufficient balance")
        balance -= amount
        print("Payment successful")
    except ValueError as e:
        print("Error:", e)

def check_balance():
    print("Current balance:", balance)

def wallet_menu():
    while True:
        print("""
--- Wallet System ---
1. Add Balance
2. Make Payment
3. Check Balance
4. Exit
""")
        try:
            choice = int(input("Choose option: "))
            if choice == 1:
                add_balance()
            elif choice == 2:
                make_payment()
            elif choice == 3:
                check_balance()
            elif choice == 4:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter a valid number")

wallet_menu()
print("Exiting Wallet System.")
