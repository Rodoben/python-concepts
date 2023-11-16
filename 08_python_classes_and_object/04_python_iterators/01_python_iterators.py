# Creating an iterator

# TO create an class/object as an iterator implement __iter__() and __next__() to object.
# __init__() function allows you to do some initializing when the object is being created.
# __iter__() method can do operations(initializing etc.), but must always return the iterator object itself.
# __next__()  method also allows you to do operations, must return the next item in the sequence.

class MyNumbers:
    def __iter__(self):
        self.a = 1  # operation(initializing)
        return self # returning the iterator object itself.
    def __next__(self):
        x = self.a
        self.a += 1
        return x
# object creation   
myclass = MyNumbers()
myiter = iter(myclass)

# type printing   
print(type(myclass))   
print(type(myiter))  

# iterator
print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))

# loop
for x in range(6):
    print(next(myiter))


# StopIteration 
# To prevent the iteration from going on forever, we can use the stopIteration statement.
# __next__() method , we can add terminating condition to raise an error.

class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
      if self.a <= 20: 
        x = self.a
        self.a += 1
        return x
      else:
         raise StopIteration 
      
# create an object of the number class
myclass = Numbers()
myiter = iter(myclass) 

print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
   print(next(myiter))