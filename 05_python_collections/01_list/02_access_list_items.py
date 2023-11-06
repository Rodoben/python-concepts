# Access List Items
# list items are indexed and you can access them by reffering to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # banana

# Negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # cherry
print(thislist[-2])  # banana

# range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])

print(thislist[-4:-1])


# check if item exist in a list using <in> Keyword
thisList = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes!, apple present in the list")
