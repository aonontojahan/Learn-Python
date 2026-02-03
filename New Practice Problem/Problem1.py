try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "1234":
        raise ValueError("Invalid login credentials")

    print("Login successful")

except ValueError as e:
    print("Error:", e)
