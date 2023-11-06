# Python - Add Set Items
# To add one item to a set use the add() method.

thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")
print(thisSet)

# update() method to add items from one set to another set
thisSet = {"apple", "banana", "cherry"}
newSet = {"kiwi", "orange", "mango"}
thisSet.update(newSet)
print(thisSet)

# Add any iterable we can make use of update() method
thisSet = {"apple", "banana", "cherry"}
myList = ["kiwi", "orange"]
thisSet.update(myList)
print(thisSet)
