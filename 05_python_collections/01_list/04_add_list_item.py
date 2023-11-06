# Python - Add list item

# append()-> To add an item to the end of the list, use the append() method
thelist = ["apple", "banana", "cherry"]
thelist.append("orange")
print(thelist)

# insert() -> To insert a list item at a specified index, use the insert() method
thelist = ["apple", "banana", "cherry"]
thelist.insert(2, "orange")
print(thelist)

# extend() -> to append elements from another list to the current list, use the extend() method.
thelist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thelist.extend(tropical)
print(thelist)
# extend() method need not only append list , it can append other data types as tuples, sets and dictionaries.
thelist = ["apple", "banana", "cherry"]
thisTuple = ("Kiwi", "orange")
thelist.extend(thisTuple)  # Tuple
print(thelist)

thelist = ["apple", "banana", "cherry"]
thisSet = {"Kiwi", "orange", "ronald"}  # appends from backward
thelist.extend(thisSet)
print(thelist)


thelist = ["apple", "banana", "cherry"]
thisSet = {"name": "ronald", "age": 36}
thelist.extend(thisSet)
print(thelist)
