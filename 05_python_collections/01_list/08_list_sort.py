# Python - Sort Lists
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)

# sort the list numbers
thisList = [100, 50, 65, 82, 23]
thisList.sort()
print(thisList)

# sorting descending
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse=True)
print(thisList)

thisList = [100, 50, 65, 82, 23]
thisList.sort(reverse=True)
print(thisList)

# Customize Sort Function
# you can also customize your own function by using the keyword argument key = function


def myfunc(n):
    return abs(n - 50)


thisList = [100, 50, 65, 82, 23]
thisList.sort(key=myfunc)
print(thisList)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Here we can use built in function as key function when sorting a list.
# make use  of str.lower

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
