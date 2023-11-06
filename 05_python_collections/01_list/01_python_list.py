# Python lists

# list are used to store multiple items in a single variable.
# one among the other build in data type in python
# Lists are created using square brackets.
# my_list = ["apple", "banana","cherry"]

my_list = ["apple", "banana", "cherry"]
print(my_list)

# list items are ordered, changeable and allow duplicate values.
# list items are indexed, first 0,second 1
# ordered -> items have defined order, order don't change,new item placed at end.
# changeable -> we can change, add and remove items in a list after creation.
# Allow Duplicates -> list is indexed, lists can have items with same value.

this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)

# length of a list
print(len(this_list))

# List items - Data Types- List items can be of different types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5, 6]
list3 = [True, False, True]
print(list1)
print(list2)
print(list3)

# A list can contain different data types:
list4 = ["Ronald", 34, True, 40, "male"]
print(list4)

# type() -> as python perspective, list are defined as object with data type 'list':
# <class 'list'>
list4 = ["Ronald", 34, True, 40, "male"]
print(type(list4))


# The list() constructor
thisList = list(("apple", "banana", "grapes"))  # note double round brackets
print(thisList)
