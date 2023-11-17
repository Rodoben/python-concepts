# Remove specified items
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

# Remove first occurence of banana
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# pop() method removes specific indexed
thisList = ["apple", "banana", "cherry"]
thisList.pop(1)
print(thisList)

# if the index is not specified in pop() method, it removes the last index
thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)


# del keyword also removes specified index:
thisList = ["apple", "banana", "cherry"]
del thisList[1]
print(thisList)

# del keyword deletes the list completely
thisList1 = ["apple", "banana", "cherry"]
del thisList1

# the list still remains but it has no content
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

duplicateList = ["a","a","b","b","a","c","c"]
removeduplicate = dict()
for x in duplicateList:
    removeduplicate[x] = True

print(removeduplicate.keys())    

for x in  removeduplicate.keys():
    print(x)
   