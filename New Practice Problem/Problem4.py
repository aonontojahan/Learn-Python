try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        data = file.read()
        print("File content loaded successfully")

except FileNotFoundError:
    print("Error: File not found")

except Exception as e:
    print("Error:", e)
