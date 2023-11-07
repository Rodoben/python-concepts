# Python if else
# python supports usual logical conditions.
# these conditions can be used in several ways, most commonly in "if statements"

a = 122
b = 30
if a > b:
    print("a is greater than b")


# Elif
# elif keyword is a python way of saying if not this then try this condition

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")

# else
a = 332
b = 33
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal a")
else:
    print("a is greater than b")

# Short hand if

if a > b:
    print("a is greater than b")

# Short hand if... else
a = 2
b = 330
print("A") if a > b else print("B")


# Multiple else statement on same line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both the conditions are true")


# or
if a > b or a > c:
    print("At least one condition is true")

# Not
# not keyword is a logical operator, used to reverse the result of the conditional statement.
a = 33
b = 200
if not a > b:
    print("a is not greater than b")

# Nested if
# if we have if statement inside if statement, we call it nested if

x = 41
if x > 10:
    print("Above 10,")
    if x > 20:
        print("and also above 20")
    if x > 30:
        print("and also above 30")
    else:
        print("but not above 40")

# Pass
# if statement cannot be empty, but if you for some reason have an if statement with no content,put the pass statement to avoid getting an error.

a = 333
b = 200
if b > a:
    pass
if a > b:
    print("a is greater than b")
