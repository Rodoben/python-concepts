# Python Json Dump Format
# indent
# to beautify and make it human readble with spaces and tabs.
import json
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

y= json.dumps(x, indent=2)
print(y)

# Separators parameter 
# default value is (", ", ": ")
y= json.dumps(x,indent=4,separators=(".","="))
print(y)

# Order the result
y = json.dumps(x, indent=4,sort_keys=True)
print(y)
