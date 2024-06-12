# return values, side effects, outputs, and whether any new objects are created.

bar = 0
foo = ['']
baz = 3
qux = (bar > baz) or bar and baz or foo

if qux:
    print("Operation succeeded")
else:
    print("Operation failed")

# So we do (bar > baz) first. This evaluates to False since 0 is not greater than 3. So now we have False or bar and baz or foo.
# because of precedence rules, instead of evaluating "False or bar"
# python evaluates "bar and baz" first
