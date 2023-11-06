# Copy a list
# list cannot be copied using = operator since i will create a reference, means changes will reflect both side

# copy() method used to copy a list from one varible to another variable
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)

myList2 = list(thisList)
print(myList2)
