# Python - Access Dictionary Items

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Get the value of key "model"
this_dict = {
    "name": "ford",
    "model": "hatchback",
    "year": 1965
}

x = this_dict["model"]
print(x)

# we can also make use of get() method to fetch the same result
x = this_dict.get("year")
print(x)

# Get Keys - keys() method will return a list of all the keys in the dictionary.
x = this_dict.keys()
print(x)

this_dict["color"] = "blue"
print(x)


# Get Values - values() method will return a list of all the values in the dictionary.
x = this_dict.values()
print(x)

# list of values is a view of the dictionary, meaning that any change done to the dictionary will be reflected in the values list.

this_dict["color"] = "red"
print(x)


# add a new key:value to the dictonary and the dict gets updated.

this_dict["doors"] = 4
print(this_dict)


# Get Items - items() method will return each item in a dictionary, as tuples in a list.

x = this_dict.items()
print(x)
print(type(x))
# returned list is a view of the items of the dictionary, meaning that any change done to the dictionary will be reflected in the items list.
this_dict["year"] = 2023
print(x)


# Check if key Exists
# to check if the key exist use in keyword:

if "model" in this_dict:
    print("Yes!, model is present in the dictonary")
