list_1 = [1, 32, 4, 5, 45, 4, 4, 3, 3, 3, 5, 6, 3, 5, 6, 343, 343, 5, 4]

divide_by_3 = []

# Without using list comprehension
for item in list_1:
    if item % 3 == 0:
        divide_by_3.append(item)

print("Without using list comprehensions:", divide_by_3)

# Using list comprehension
print("Using List comprehensions:",
      [item for item in list_1 if item % 3 == 0])