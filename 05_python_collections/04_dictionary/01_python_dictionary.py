# Python Dictornaries
# Dictionaries are used to store data vales in <key:value> pairs
# dictionary is a collection which is ordered, changeable and do not allow duplicates.
# dictionary are written with curly brackets, and have keys and values:

thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1965
}

print(thisDict)

# Dictionary can be reffered to by using the key name:
print(thisDict["brand"])
print(thisDict["model"])
print(thisDict["year"])

# Before 3.6 the dictionaries are unordered.
# when we say dictionaries are ordered, it means that the items have a defined order and the order will not change.
# Unordered means that the items does not have a definite order, you cannot refer to an item by using an index.
# thisDict[1]= "bmw"   we cannot do this
# Dictionaries items are changeable, i.e we can add , remove and change the dictionary after it is created.
thisDict["brand"] = "BMW"
print(thisDict)
# Dictionaries do not allow duplicates
thisDict = {
    "model": "ford",
    "brand": "Mustang",
    "year": 1987,
    "year": 2020
}
print(thisDict)

# length of the dictionary
print(len(thisDict))


# type of the dictionary <class "set">
print(type(thisDict))

# dict() constructor

thisDict = dict(
    name="ronald",
    age=36,
    country="india"
)
print(thisDict)
