# convert from python object to json string

import json

x = {
    "name":"Ronald",
    "age":60,
    "city": "New York",
    "companies":["tcs","ibm","GL"]
}

print(type(x))
y = json.dumps(x)
print(y)
print(type(y))

# we can covert the following types into json string.
# dict,tuple,list,string,int,float,boolean, none.
# We canot convert a set datatype to string
# mySet = {"name","age","city"}
# print(type(mySet))
# print(mySet)
# y = json.dumps(mySet)
# print(y)
# print(type(y))


#convert a dict to json string
x = {"name":"ronald","age":30,"city":"Bangalore"}
y = json.dumps(x)
print(type(y))
print(y)
# convert a tuple to json string
x = ("name","age","city")
y = json.dumps(x)
print(type(y))
print(y)
# convert a list to json string
x = ["name","age","city"]
y = json.dumps(x)
print(type(y))
print(y)

# convert an int to json string
x = 1
y = json.dumps(x)
print(type(y))
print(y)
# convert a float to json string
x = 1.23
y = json.dumps(x)
print(type(y))
print(y)
# convert a string to json string
x = "ronald"
y = json.dumps(x)
print(type(y))
print(y)
# convert a boolean to json string
x = True
y = json.dumps(x)
print(type(y))
print(y)

# convert a None to json string
x = None
y = json.dumps(x)
print(type(y))
print(y)

# All valid datatypes grouped together to convert into json string
x = {
    "name":"ronald",
    "age":30,
    "married": True,
    "divorced": False,
    "children": ("ann","belly"),
    "pets": None,
    "cars": [{"model":"BMW 230","mpg":27.6},
             {"model":"BMW 230","mpg":27.6},
            ]
}

print(json.dumps(x))
print(type(json.dumps(x)))

