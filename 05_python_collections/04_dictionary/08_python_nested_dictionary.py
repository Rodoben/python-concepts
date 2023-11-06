# Python - Nested Dictionary
# A dictionary can contain dictionaries, this is called nested dictionaries.

# create a dictionary that contains three dictionaries.

myfamily = {
    "child1": {
        "name": "ronald",
        "year": 12
    },
    "child2": {
        "name": "ronald",
        "year": 12
    },
    "child3": {
        "name": "ronald",
        "year": 12
    }
}

print(myfamily)


# create 3 dictonaries and add in one dictionary

emp1 = dict(name="ronald", age=34)
emp2 = dict(name="donald", age=24)
emp3 = dict(name="derek", age=44)

employee = {
    "emp1": emp1,
    "emp2": emp2,
    "emp3": emp3,
}

print(employee)


# to access the item from a nested dictionary, you use the name of the dictionaries, starting with outer dictionary:
print(myfamily["child3"]["name"])

print(employee["emp2"]["name"])
