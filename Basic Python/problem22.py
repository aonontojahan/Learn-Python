# ATM Simulation using if-else

balance = 10000

print("===== ATM MENU =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Your Balance =", balance)

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful!")
        print("Updated Balance =", balance)
    else:
        print("Invalid deposit amount!")

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid withdrawal amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdraw successful!")
        print("Remaining Balance =", balance)

elif choice == 4:
    print("Thank you for using ATM. Goodbye!")

else:
    print("Invalid choice! Please select option 1-4.")
