# Nested loop with if-else example:
# Prints multiplication table from 1 to 5,
# and highlights even numbers.

for i in range(1, 6):           # Outer loop
    for j in range(1, 6):       # Inner loop
        result = i * j
        if result % 2 == 0:     # Conditional check
            print(f"{i} x {j} = {result} (even)")
        else:
            print(f"{i} x {j} = {result}")
    print()  # blank line after each row
