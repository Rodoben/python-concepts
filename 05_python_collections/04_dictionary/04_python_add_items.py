# Python - Add Dictionary items
# Adding items
# adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

thisDict["color"] = "red"
print(thisDict)

# Update() method will update the dictionary with the items from a given arguments.
# if the item does not exist the item will be added.

thisDict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1965
}
# this item is not present hence added newly
thisDict1.update({"color": "red"})
# this makes the changes
thisDict1.update({"year": 2023})
print(thisDict1)
