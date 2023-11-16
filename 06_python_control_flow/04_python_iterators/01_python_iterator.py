# Python Iterators
# An Iterator is an object which contains countable number of values.
# Iterator is an object that can be iterated upon, meaning you can traverse through all the values.
# An Iterator is an object which implement iterator protocol.
# consist of methods __iter__() and __next__().

# Iterator v/s Iterable
# List , tuples, dictionaries and sets are all iterable objects.
# They are iterable containers which you get an iterator. 

myTuple = ("apple","banana","cherry")
mySet = {"apple","banana","cherry"}

myit = iter(myTuple)
mysetit = iter(mySet)

print(type(mysetit))
print(type(myit))

print(next(myit))
print(next(myit))
print(next(myit))

for x in range(3):
    print(next(mysetit))

# Strings are iterable objects, containing a sequence of characters.
mystr = "banana"
myit = iter(mystr)   

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit)) # more number of print statement is an error.


# We can also make use of for loop to iterate over an iterable object:
myTuple = ("apple","banana","cherry")
for x in myTuple:
    print(x)