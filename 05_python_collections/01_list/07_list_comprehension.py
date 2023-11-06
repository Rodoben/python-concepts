# Python-List comprehension
# list comprehension offers a shorter syntax when new list created based on values of existing list.
# without list comprehension. syntax below.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# with the use of list comprehension you can do it with one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = [x for x in fruits if "a" in x]
print(newList)

# newList = [expression for item in iterable if condition == True]

newList = [x for x in fruits if "a" not in x]
print(newList)

newList = [x for x in fruits if x != "apple"]
print(newList)

newlist = [x for x in fruits]
print(newList)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
newList = [x for x in range(10)]
print(newList)

newList = [x for x in range(10) if x < 5]
print(newList)

# Expression
# expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
newList = [x.upper() for x in fruits]
print(newList)

# you can set the outcome to whatever you like:
newList = ["Hello" for x in fruits]
print(newList)

newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)
