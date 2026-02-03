try:
    marks = int(input("Enter student marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 80:
        grade = "A+"
    elif marks >= 70:
        grade = "A"
    elif marks >= 60:
        grade = "A-"
    else:
        grade = "Fail"

    print("Grade:", grade)

except ValueError as e:
    print("Input error:", e)
