# Tuples
# tuples are used to store multiple items in a single variable
# tuple is a collection which is ordered and unchangeable
# tuples are written with round brackets ()

thisTuple = ("apple", "banana", "cherry", "mango")
print(thisTuple)

# Tuple items are ordered, unchangeabe and allow duplicate values
# Tuples are indexed, first item has index[0] andsecond one as index [1]
print(thisTuple[1])
# tuple items are ordered, it means that the items have a definite order, and the order will not change.
# TUPLES ARE UNCHANGEABLE, MEANING THAT WE CANNOT CHANGE, ADD OR REMOVE ITEMS AFTER THE TUPLE HAS BEEN CREATED.
# thisTuple[1] = "grapes"  we cannot change the tuple
# print(thisTuple)
# Tuple are indexed hence it can allow duplicates.
thisTuple = ("apple", "banana", "cherry", "mango", "mango")
print(thisTuple)

# length of the tuple len()
thisTuple = ("apple", "banana", "cherry", "mango", "mango")
print(len(thisTuple))

# Create a tuple with one item
# one item tuple, remember comma(,)
thisTuple1 = ("apple")  # this is not a tuple but string
print(type(thisTuple1))

thisTuple2 = ("apple",)
print(type(thisTuple2))  # this is a tuple since there is comma(,)

# Tuple items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3, 4, 5, 6)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# tuple can hold items of different data types
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)

# type() tuples are defined as objects with the datatype 'tuple':
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# tuple() constructor
thisTuple = tuple(("apple", "banana", "cherry"))
print(thisTuple)
