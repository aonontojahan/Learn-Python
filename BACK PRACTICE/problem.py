# School Marks Processing System
# Uses nested loops + if/else
# Multi-class, multi-student, multi-subject evaluation

# ------------------------------
# Sample dataset
# ------------------------------
# Format:
# {
#   "ClassName": [
#       {"name": "StudentA", "marks": [m1, m2, m3]},
#       ...
#   ],
#   ...
# }

school = {
    "Class-1": [
        {"name": "Alice", "marks": [78, 85, 92]},
        {"name": "Bob", "marks": [55, 64, 71]},
        {"name": "Carol", "marks": [90, 93, 95]}
    ],
    "Class-2": [
        {"name": "David", "marks": [45, 52, 49]},
        {"name": "Eva", "marks": [88, 90, 84]},
        {"name": "Frank", "marks": [70, 68, 66]}
    ],
    "Class-3": [
        {"name": "Grace", "marks": [95, 97, 94]},
        {"name": "Henry", "marks": [58, 60, 62]},
        {"name": "Ivy", "marks": [77, 81, 79]}
    ]
}

# ------------------------------
# Part 1: Compute student stats
# ------------------------------
print("Student Results:\n")
overall_topper = {"name": None, "total": -1, "class": None}

for class_name, students in school.items():  # Outer loop: classes
    print(f"Processing {class_name}:")
    
    class_totals = []
    class_topper = {"name": None, "total": -1}
    
    for student in students:                 # Inner loop: students
        marks = student["marks"]
        total = sum(marks)
        average = total / len(marks)
        
        # Classification via if/else
        if average >= 60:
            status = "PASS"
        else:
            status = "FAIL"
        
        # Track class totals for later stats
        class_totals.append(total)
        
        # Track class topper
        if total > class_topper["total"]:
            class_topper = {"name": student["name"], "total": total}
        
        # Track overall topper
        if total > overall_topper["total"]:
            overall_topper = {"name": student["name"], "total": total, "class": class_name}
        
        print(f"  {student['name']}: Marks={marks}, Total={total}, Avg={average:.2f}, Status={status}")
    
    print()
    
    # ------------------------------
    # Part 2: Class statistics
    # ------------------------------
    highest = max(class_totals)
    lowest = min(class_totals)
    avg_class = sum(class_totals) / len(class_totals)
    
    print(f"Class Summary for {class_name}:")
    print(f"  Highest Total: {highest}")
    print(f"  Lowest Total: {lowest}")
    print(f"  Average Total: {avg_class:.2f}")
    print(f"  Class Topper: {class_topper['name']} with {class_topper['total']} marks\n")
    print("-" * 50)

# ------------------------------
# Part 3: Overall School Topper
# ------------------------------
print("\nOverall School Topper:")
print(f"  Name: {overall_topper['name']}")
print(f"  Total Marks: {overall_topper['total']}")
print(f"  Class: {overall_topper['class']}")
