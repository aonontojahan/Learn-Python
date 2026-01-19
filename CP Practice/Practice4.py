n = int(input())

total_users = n
blocked_users = 0
total_fine_collected = 0

student_count = 0
faculty_count = 0

for user_index in range(1, n + 1):

    user_id, user_type, books = input().split()
    user_type = int(user_type)
    books = int(books)

    print("User ID:", user_id)

    # User type check
    if user_type == 1:
        user_category = "Student"
        max_books = 3
        student_count += 1
    else:
        if user_type == 2:
            user_category = "Faculty"
            max_books = 5
            faculty_count += 1
        else:
            user_category = "Unknown"
            max_books = 0

    print("User Type:", user_category)

    # Book limit validation
    if books > max_books:
        print("Status: Blocked (Book limit exceeded)")
        blocked_users += 1

        # Still need to read inputs to avoid input mismatch
        for skip in range(books):
            input()

        print("----------------------------")
        continue
    else:
        print("Book Limit OK")

    user_fine = 0

    # Process each book
    for book_index in range(1, books + 1):

        days = int(input())
        fine = 0

        if days <= 7:
            fine = 0
        else:
            if days <= 15:
                extra_days = days - 7
                fine = extra_days * 2
            else:
                extra_days = days - 15
                fine = (8 * 2) + (extra_days * 5)

        print("Book", book_index, "Days:", days, "Fine:", fine)

        user_fine = user_fine + fine

    print("Total Fine for User:", user_fine)
    total_fine_collected = total_fine_collected + user_fine

    print("----------------------------")

# Final Report
print("====== LIBRARY SUMMARY ======")
print("Total Users:", total_users)
print("Blocked Users:", blocked_users)
print("Students:", student_count)
print("Faculty:", faculty_count)
print("Total Fine Collected:", total_fine_collected)
