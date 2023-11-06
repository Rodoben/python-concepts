# Python Copy Dictionary
# Copy a Dictionary
# we cannot copy a dictionary using =  operator (dict1=dict2), cuz it will be only referenced and the changes will be done mutually

# copy()
thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1965
}

mydict = thisDict.copy()
print(mydict)

# dict()
thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1564
}

mydict = dict(thisDict)
print(mydict)
