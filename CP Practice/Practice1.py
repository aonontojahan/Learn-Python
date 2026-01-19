n = int(input())

pass_count = 0
fail_count = 0

for i in range(1, n + 1):
    m1, m2, m3 = map(int, input().split())

    failed = False

    if m1 < 40:
        failed = True
    else:
        if m2 < 40:
            failed = True
        else:
            if m3 < 40:
                failed = True

    if failed:
        print("Student", i, ": Fail")
        fail_count += 1
    else:
        total = m1 + m2 + m3
        avg = total / 3

        if avg >= 75:
            grade = "A"
        else:
            if avg >= 60:
                grade = "B"
            else:
                if avg >= 50:
                    grade = "C"
                else:
                    grade = "D"

        print("Student", i, ": Pass Grade", grade)
        pass_count += 1

print("Passed:", pass_count)
print("Failed:", fail_count)
