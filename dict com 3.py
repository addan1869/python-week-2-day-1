students = ["Ali", "Ahmed", "Addan", "Sara"]
marks = [85, 90, 78, 88]

# Without Dictionary Comprehension
result = {}

for i in range(len(students)):
    result[students[i]] = marks[i]

print("Without Dictionary Comprehension:", result)

# With Dictionary Comprehension
result = {students[i]: marks[i] for i in range(len(students))}

print("With Dictionary Comprehension:", result)