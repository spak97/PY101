numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(numbers[::-1])

numbers.reverse()
print(numbers)

#2
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

number1 in numbers  
number2 in numbers  

#3
42 in range(10, 101)
100 in range(10, 101)
101 in range(10, 101)

#4
l = [1, 2, 3, 4, 5]
del l[2]