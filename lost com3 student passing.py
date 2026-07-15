marks = [45, 67, 30, 89, 55, 40, 90]

# Without List Comprehension
passing = []
for mark in marks:
    if mark >= 50:
        passing.append(mark)

print("Without List Comprehension:", passing)

# With List Comprehension
passing = [mark for mark in marks if mark >= 50]

print("With List Comprehension:", passing)