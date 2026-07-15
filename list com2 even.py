numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without List Comprehension
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)

print("Without List Comprehension:", even)

# With List Comprehension
even = [i for i in numbers if i % 2 == 0]

print("With List Comprehension:", even)