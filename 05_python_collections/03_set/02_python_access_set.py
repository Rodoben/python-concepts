# Python - Access Set Items
# you cannot access items in a set by referring to an index or a key.
# we have two inbuilt keywords
# for -> to loop over the set
# in -> to check if the value is present in the set

thisSet = {"apple", "banana", "cherry"}
for x in thisSet:  # for keyword to range over the set
    print(x)


print("banana" in thisSet)  # in keyword to check if the item exist in the set.
