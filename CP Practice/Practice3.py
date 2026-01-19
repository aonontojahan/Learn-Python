n = int(input())

total_students = n
disqualified = 0
passed = 0
failed = 0

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0

for student_index in range(1, n + 1):

    student_id, attendance = input().split()
    attendance = int(attendance)

    marks = list(map(int, input().split()))

    print("Student ID:", student_id)

    # Attendance check
    if attendance < 75:
        print("Status: Disqualified due to low attendance")
        disqualified += 1
        print("----------------------------")
        continue
    else:
        print("Attendance OK")

    # Marks validation
    has_failed_subject = False

    for mark in marks:
        if mark < 40:
            has_failed_subject = True
            break
        else:
            pass

    if has_failed_subject:
        print("Result: Fail (One or more subjects below 40)")
        failed += 1
        print("----------------------------")
    else:
        total = 0

        for m in marks:
            total = total + m

        average = total / 5

        print("Average Marks:", average)

        if average >= 80:
            grade = "A"
            grade_a += 1
        else:
            if average >= 65:
                grade = "B"
                grade_b += 1
            else:
                if average >= 50:
                    grade = "C"
                    grade_c += 1
                else:
                    grade = "D"
                    grade_d += 1

        print("Result: Pass")
        print("Grade:", grade)
        passed += 1
        print("----------------------------")

# Final Summary
print("====== FINAL SUMMARY ======")
print("Total Students:", total_students)
print("Disqualified:", disqualified)
print("Passed:", passed)
print("Failed:", failed)

print("Grade A:", grade_a)
print("Grade B:", grade_b)
print("Grade C:", grade_c)
print("Grade D:", grade_d)
