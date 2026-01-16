# Python 3 Program: Student Result with Grading using if-else

print("Enter marks for five subjects out of 100:")

math = float(input("Math: "))
physics = float(input("Physics: "))
chemistry = float(input("Chemistry: "))
english = float(input("English: "))
computer = float(input("Computer: "))

# Calculate total and percentage
total = math + physics + chemistry + english + computer
percentage = total / 5

# Determine grade using if-else chain
if percentage >= 90 and percentage <= 100:
    grade = "A+"
elif percentage >= 80 and percentage < 90:
    grade = "A"
elif percentage >= 70 and percentage < 80:
    grade = "B"
elif percentage >= 60 and percentage < 70:
    grade = "C"
elif percentage >= 50 and percentage < 60:
    grade = "D"
elif percentage >= 0 and percentage < 50:
    grade = "F (Fail)"
else:
    grade = "Invalid percentage (Check input!)"

# Output results
print("\n----- RESULT -----")
print("Total Marks =", total)
print("Percentage =", percentage, "%")
print("Grade =", grade)
