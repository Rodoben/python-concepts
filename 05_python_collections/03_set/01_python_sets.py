# Python sets
# sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable and unindexed.
# sets are written in curly brackets

thisSet = {"apple", "banana", "cherry"}
print(thisSet)

# set items are unordered, unchangeable and do not allow duplicate values.
# unordered means that the items in a set do not have a defined order.
# unchangeble, meaning we cannot change the item after it has been created.
# duplicates not allowed, hence duplicated are ignored.

thisSet = {"apple", "banana", "cherry", "cherry"}
print(thisSet)


# True and 1 is considered the same value:
thisSet = {"apple", "banana", "cherry", True, 1, 2}
print(thisSet)

# False and 0 is considered to be the same value.
thisSet = {"apple", "banana", "cherry", False, 0, 2}
print(thisSet)


# get the length of the set
thisSet = {"apple", "banana", "cherry"}
print(len(thisSet))

# set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 5, 6, 7, 0, 0}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)


# type() <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))


# The set constructor
mySet = set(("apple", "banana", "cake", "cake"))
print(mySet)
