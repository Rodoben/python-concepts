# Python Json
# json is a syntax for storing and exchanging data.
# json is text, written with javascript object notation.

# python has a built-in package json, which can be used to work with json.

import json

x = '{"name":"ronald","age":30,"city":"Bangalore"}'
print(x)
print(type(x))

y = json.loads(x) # convert json string to python object
print(y)
print(type(y))
print(y["age"])
print(y["name"])
print(y["city"])