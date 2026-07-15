square = {}

for i in range(1, 6):
    square[i] = i * i

print("Without Dictionary Comprehension:", square)

square = {i: i * i for i in range(1, 6)}

print("With Dictionary Comprehension:", square)