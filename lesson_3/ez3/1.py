numbers = [1, 2, 3, 4]

numbers.clear


for _ in range(len(numbers)):
    numbers.pop()

print(numbers)

# or
while numbers:
    numbers.pop()