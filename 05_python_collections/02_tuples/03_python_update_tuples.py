# Update Tuples

# Tuples are unchangeable, meaning that you cannot change, add or remove items once the tuples is created.
# To update a tuple first change it to list, make the chnages and convert it to the tuple

x = ("apple", "banana", "cherry")
print(type(x))
y = list(x)
y[1] = "pineapple"
print(type(y))
x = tuple(y)
print(x)
print(type(x))

# to add into a tuple, we don't have append() method so we can first convert into list
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
y.insert(2, "grapes")
print(y)
print(type(y))
x = tuple(y)
print(x)
print(type(x))

# add tuple to a tuple
x = ("apple", "banana", "cherry")
y = ("orange",)
x = x + y
print(x)

# remove an item from a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

# clear a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.clear()
print(y)
x = tuple(y)
print(x)
