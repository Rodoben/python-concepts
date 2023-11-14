# Python class and object
# python is an object oriented programming language
# A class is an object constructor, or a blueprint for creating objects.
# Almost everything in python is an object with its funtion and methods.

# create a class < use keyword class>
class MyClass:
    x = 5

# To create an object
class1 = MyClass()
print(class1.x)    

# The _init_() function
# All classes have a function called _init_(), which is always executed when the class is being initiated.
# _init_() function is used to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
    def __init__(self,name,age):
          self.name = name
          self.age = age

p1 = Person("John",35) 
print(p1) # string representation of the object is returned
print(type(p1))
print(p1.name)
print(p1.age)
print(type(p1.name))
print(type(p1.age))

# The _str_() function
# used to control the return value when the class object is represented as a string.

class Employee:
    def __init__(self,name,age):
         self.name = name
         self.age = age

    def __str__(self): # controlled the return value and represented as a sting
         return f"{self.name}({self.age})"     
    
p1 = Employee("John",36)
print(p1)    
print(type(p1))
print(p1.name)
print(p1.age)
print(type(p1.name))
print(type(p1.age))

# Object Method
# Objects can also contain method. Methods in objects are functions that belong to the object.

class Monitor:
    def __init__(self,brand,size,resolution):
          self.brand = brand
          self.size = size
          self.resolution = resolution 
    def DisplayMonitor(self):
         print("Hello! The Monitor brand is "+ self.brand+" with size "+ self.size,"and resolution "+ self.resolution)

monitor1 = Monitor("LG","34 inches", "4k")         
print(monitor1)

monitor1.DisplayMonitor()

# The Self Parameter
# The self parameter is a reference to the current instance of the class which is used to access variables to the class.
# Not neccesary to name it self, it could be anything but the first parameter of any function in the class.

class Person:
    def __init__(mysillyobject,name,age):
          mysillyobject.name = name
          mysillyobject.age = age
    def myfunc(mysillyobject):
         print("Hello my name is "+ mysillyobject .name, " age " + str(mysillyobject.age))

p1 = Person("Ronald",26)
p1.myfunc()  


# Modify Object Properties
p1.age = 40
p1.myfunc()  

# Delete object properties <use del keyword>
del p1.age
p1.myfunc()  

# Delete Objects 
del p1

# class cannot be empty, but if it is, we put <pass> to avoid getting error.
class Person:
     pass