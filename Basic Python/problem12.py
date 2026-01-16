# Restaurant Billing System using if-else

print("===== RESTAURANT MENU =====")
print("1. Burger  = 120")
print("2. Pizza   = 250")
print("3. Pasta   = 180")
print("4. Coke    = 50")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    qty = int(input("Enter quantity: "))
    total = 120 * qty
    print("Total Bill =", total)

elif choice == 2:
    qty = int(input("Enter quantity: "))
    total = 250 * qty
    print("Total Bill =", total)

elif choice == 3:
    qty = int(input("Enter quantity: "))
    total = 180 * qty
    print("Total Bill =", total)

elif choice == 4:
    qty = int(input("Enter quantity: "))
    total = 50 * qty
    print("Total Bill =", total)

elif choice == 5:
    print("Thank you! Visit again.")

else:
    print("Invalid choice! Please select item from the menu.")
