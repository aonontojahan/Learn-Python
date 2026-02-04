students = {}  # in-memory database


def add_student():
    try:
        student_id = input("Enter Student ID: ")

        if student_id in students:
            raise ValueError("Student ID already exists")

        name = input("Enter Student Name: ")
        cgpa = float(input("Enter CGPA (0.0 - 4.0): "))

        if cgpa < 0 or cgpa > 4:
            raise ValueError("CGPA must be between 0.0 and 4.0")

        students[student_id] = {
            "name": name,
            "cgpa": cgpa
        }

        print("Student added successfully")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)


def view_students():
    try:
        if not students:
            raise LookupError("No student records found")

        print("\n--- Student List ---")
        for sid, info in students.items():
            print(f"ID: {sid}, Name: {info['name']}, CGPA: {info['cgpa']}")

    except LookupError as e:
        print(e)


def calculate_average_cgpa():
    try:
        if not students:
            raise ZeroDivisionError("No students available to calculate CGPA")

        total = sum(student["cgpa"] for student in students.values())
        average = total / len(students)

        print("Average CGPA:", round(average, 2))

    except ZeroDivisionError as e:
        print("Error:", e)


def main_menu():
    while True:
        print("""
--- Student Management System ---
1. Add Student
2. View Students
3. Calculate Average CGPA
4. Exit
""")
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                calculate_average_cgpa()
            elif choice == 4:
                print("Exiting system...")
                break
            else:
                print("Invalid option. Please choose 1-4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the system
main_menu()
