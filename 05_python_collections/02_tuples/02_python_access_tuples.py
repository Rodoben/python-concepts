# Accessing Tuple Items

# you can access tuple items by referring to the index number, inside square brackets:

thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1])

# negative indexing
print(thisTuple[-1])

# Range of indexes
# you can specify a range of indexes by specifying where to start and where to end the range.
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[2:5])
# ending indexes slice
print(thisTuple[:4])
# starting indexes slice
print(thisTuple[2:])
#  negative index slice
print(thisTuple[-4:-1])


# Check if item exist in tuple:

thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
    print("Yes,\"apple\" is in the fruits tuple")
