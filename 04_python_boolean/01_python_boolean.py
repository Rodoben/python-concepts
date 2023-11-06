# python booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

# print a message based on whether the condition is True or False:
a = 200
b = 333

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#  Evaluate values and variables.
#  bool() function allows you to evaluate any value and return true or false.
# Almost any value is evaluated to True if it has some sort of content.
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Any string is True, except empty strings.
print("Any string is True, except empty strings.")
print(bool(""))

# Any number is True, except 0.
print("Any number is True, except 0.")
print(bool(0))

# Any list, tuple, set, and dictionary are True, except empty ones.
print("Any list, tuple, set, and dictionary are True, except empty ones.")
print(bool(["ron", "don"]))
print(bool(("ron", "don")))
print(bool({"ron", "don"}))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

print("_____________________________")

# One more value, or object in this case, evaluate to False, and that is if you have an object that is made from a class with a _len_ function that returns 0 or false.


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# Function can return boolean:


def myFunction():
    return True


print(myFunction())
print(bool(myFunction()))

# you can execute code based on the boolean answer of a function:

if myFunction():
    print("Yes")
else:
    print("No!")

# check if an object is an integer or not
x = 200
print(isinstance(x, int))
