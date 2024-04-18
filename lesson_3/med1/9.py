def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

bar(foo())

# no

# 10
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# all the same