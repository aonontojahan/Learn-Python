marks = []

for i in range(5):
    m = int(input(f"Enter marks {i+1}: "))
    marks.append(m)

print("Marks:", marks)
print("Average:", sum(marks) / len(marks))
