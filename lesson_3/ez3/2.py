print([1, 2, 3] + [4, 5])

# [1, 2, 3, 4, 5]

#3
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# 'hello there'

#4
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

#prints original. Doesn't mutate because nested elements are not deep copied.
# nevermind, I was right that there is no deep copy, but that is actually why it's mutated.
# shallow copy means the object itself isn't copied into the new variable. Just the pointer is copied instead
