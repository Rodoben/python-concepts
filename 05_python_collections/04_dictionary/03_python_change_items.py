# Python - Change Dictionnary items
# you can change the value of a specified item by referring to its key name:

thisDict = {
    "name": "ford",
    "model": "Mustang",
    "year": 1964
}

thisDict["year"] = 2023

print(thisDict)

# update() method will update the dictionary with the items from given argument
# the arguments must be a dictionary, or an iterable object with <key:value> pairs.

thisDict.update({"model": "hatchback"})
print(thisDict)
