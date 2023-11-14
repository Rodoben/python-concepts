# Python Polymorphism
# The word polymorphism means many forms
# In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# len() function can be used on different objects

x = "Hello World!"
print(len(x))

mytuple = ("apple","banana","cherry","cherry")
print(len(mytuple))

myset = {"apple","banana","cherry","cherry"}
print(len(myset))

thisDict = {
    "brand": "ford",
    "model":"Mustang",
    "year":1964,
    "wheels":4
}

print(len(thisDict))

# Polymorphism is often used in class method, where we can have multiple classes with the same method name.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self,brand ,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")       

car1 = Car("Ford","mustnag")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing","747")      

car1.move()
boat1.move()
plane1.move()

for x in (car1,boat1,plane1):
    x.move()


# Inheritance class polymorphism
# What about classes with child classes with the same name? can we use polymorphism there?
# Yes! we can make a base class and define derived class with different base class name.
# the child class inherits the base class methods, but can override them.
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass # inherits the vehicle class method, i.e move() function
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
     def move(self):
        print("Fly!") 

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing","747")   

car1.move()


for x in (car1,boat1,plane1):
    print(x.brand, x.model)
    x.move()
