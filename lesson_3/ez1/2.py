str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation(str):
    return str[-1] == '!'

print(exclamation(str1))
print(exclamation(str2))

# Or .endswith()