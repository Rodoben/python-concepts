# Python - Loop Dictionaries
# you can loop through a dictionary using a for loop.

thisDict = {
    "name": "ford",
    "model": "habibi",
    "year": 1987
}

# print all the key names
for x in thisDict:
    print(x)
print("_____________________")
# print all the values in the dictionary
for x in thisDict:
    print(thisDict[x])

print("_____________________")
# print the values() method to return values of a dictionary:
for x in thisDict.values():
    print(x)
print("_____________________")
# keys() method to return the keys of a dictionary:
for x in thisDict.keys():
    print(x)


# items() method loops through both keys and values
for x, y in thisDict.items():
    print(x, y)
