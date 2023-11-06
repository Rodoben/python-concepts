# Python - Remove Dictionary Items
# There are several methods to remove items from a dictionary.

# 1 pop() method with specified key name

thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1976
}

thisDict.pop("model")
print(thisDict)

# 2 popitem() method removes the last inserted item.

thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1976
}

thisDict.popitem()
print(thisDict)

# 3 del keyword with specified key name:

thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1976
}
del thisDict["model"]
print(thisDict)


# 4 clear() method empties the dictionary

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.clear()
print(thisDict)
