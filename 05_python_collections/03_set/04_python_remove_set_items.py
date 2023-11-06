# Python - Remove set items
# to remove an item from a set, we make use of two methods
# remove() and discard()
# remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# we have an option to remove an item using pop(), but randomly removes an item from the set
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

# Clear method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()  # set()
print(thisset)


# del keyword deleted tye set completely
thisset = {"apple", "banana", "cherry"}
del thisset  # this List does not exist anymore due to del keyword.
