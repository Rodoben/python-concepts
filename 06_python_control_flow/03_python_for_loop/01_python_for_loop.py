# Python For Loops
# A for loop is used to iterate over a sequence (i.e list, tuple, dictionary, set or a string)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# iterating over a string.
name = "Ronald"
for x in name:
    print(x)

# The break statement.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print("_______________________")
# The continue statement.
fruits = ["apple", "banana", "cherry"]
for x in fruits:

    if x == "banana":
        continue
    print(x)

# The range() function
# to loop through a set of code a specified number of times, we cna use the range() function.
# range() function returns a equence of numbers, default 0 increment by 1

for x in range(6):
    print(x)

print("_______________________")
for x in range(2, 6):
    print(x)
print("_______________________")
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

# Else in for loop
# else keyword in a for loop specifies a block of code to be executed when the loop is finished.

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# else block is not executed if the loop is stopped by break statement.
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# Nested Loops
# a nested loop is a loop inside a loop
# the inner loop will be executed one time for each iteration of the outer loop:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# Pass statement.
# for loops cannot be empty, but incase the loop is with no content, put in the pass statement.
for x in [0, 1, 2]:
    pass
