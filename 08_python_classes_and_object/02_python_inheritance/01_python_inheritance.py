# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class -> class being inherited from, base class.
# Child class -> class that inherits from another class, derived class.


# Create a Parent class.
class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname,self.lastname)
x = Person("John","Doe")
x.printname()        

# Create a child class.
# To create a class that inherits the functionality from another class as a parameter when creating the child.
class Student(Person):
    pass  # when we do not want to specify any content in this class, to avoid error.
y = Student("Ronald","Benjamin")
y.printname()

# Add the __init__() function.
# when we add _init_() function, the child will no longer inherit the parent _init_() function

class Mobile:
    def __init__(self,brand,size,colour,storage,ram):
        self.brand = brand
        self.size = size
        self.colour = colour
        self.storage = storage
        self.ram = ram

    def printMobile(mobile):
        print("Mobile specs:",mobile.brand,mobile.size,mobile.colour,f"{mobile.storage}GB Storage",f"{mobile.ram}GB RAM")    

m1 = Mobile("Apple 14 pro","6.1 inches", "black","512","8")
m1.printMobile()

class BarPhone(Mobile):
     def __init__(self,brand,size,colour,storage,ram):
        self.brand = brand
        self.size = size
        self.colour = colour
        self.storage = storage
        self.ram = ram

b1 = BarPhone("Apple 15 pro","6.1 inches", "black","512","8")
b1.printMobile()

# To keep the inheritance of the parent __init__() function, add a call to the parent __init__() function:

class Mobile:
    def __init__(self,brand,size,colour,storage,ram):
        self.brand = brand
        self.size = size
        self.colour = colour
        self.storage = storage
        self.ram = ram
    def printMobile(mobile):
        print("Mobile specs:",mobile.brand,mobile.size,mobile.colour,f"{mobile.storage}GB Storage",f"{mobile.ram}GB RAM")    
m1 = Mobile("Apple 14 pro","6.1 inches", "black","512","8")
m1.printMobile()

class BarPhone(Mobile):
     def __init__(self,brand,size,colour,storage,ram):
       Mobile.__init__(self,brand,size,colour,storage,ram)
b1 = BarPhone("Apple 15 pro","6.1 inches", "black","512","8")
b1.printMobile()

# Use the super() function.
# Allows the child class to inherit all the methods and properties from its base class.

class Animal:
    def __init__(self,firstname):
        self.firstname= firstname

    def speak(self):
       print("Hello I am "+self.firstname) 
            
class Bird(Animal):
    def __init__(self,firstname,wingspan):
        super().__init__(firstname) # inherited all the properties and method of base class
        self.wingspan = wingspan
        self.legs = 2  # Adding properties

    def fly(self): # Adding methods
        print(f"{self.firstname} is flying with wingspan of {self.wingspan} units")    
Animal1 = Animal("Generic animal")
Bird1 = Bird("Sparrow",10)
Animal1.speak() 
Bird1.speak()
Bird1.fly()
print(Bird1.legs)



