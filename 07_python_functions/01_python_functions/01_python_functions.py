# Python Functions
# a function is a block of code which only runs when it is called.
# we can pass data, known as parameters, into a function and can return data as a result.
# In python a function is defined using the def keyword.

def my_function():
    print("Hello from a function")


# to call the above function
my_function()

# Arguments
# Information can be passed into a function as arguments.
# Arguments are specified after the function name, inside the paranthesis. def funcName(args)


def my_function(fname):
    print("Hello", fname)


my_function("ronald")
my_function(12)


def even(nums):
    rnum = []
    for x in nums:
        if x % 2 == 0:
            rnum.append(x)
    print(rnum)


even([1, 2, 3, 4, 5, 6, 7, 8])
# A parameter is the variable listed inside the paranthesis in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of arguments


def my_function2(fname, lname):
    print(fname+" "+lname)


my_function2("Ronald", "Benjamin")

# Arbitary Arguments , *args
# to send multiple arguments we can use *args in function definition
# the function will recieve tuple of arguments


def my_function3(*kids):
    print(type(kids))
    for x in kids:
        print(x)


my_function3("ronald", "derek", "linus")


# Keyword Arguments
# you can also send arguments with the key = value syntax
# this way the order of the argument does not matter.

def my_function(child3, child2, child1):
    print(type(child1))
    print(type(child2))
    print(type(child3))
    print("The youngest child is "+child3)


my_function(child1="ronald", child2="benjamin", child3="derek")


# Arbitrary keyword argument, **Kwargs (dictionary of argument)
def my_function(**kid):
    print(type(kid))
    print("His last name is "+kid["lname"])


my_function(fname="Ronald", lname="Benjamin")

# Default parameter value:
# if we do function call with no arguments, it uses default value:


def my_function(county="Norway"):
    print("I am from " + county)


my_function("Sweden")
my_function()

# Passing a List as an Argument
# we can send any data types of argument to a function(string, number, list, dictionary)
# and it will be treated as the same data type inside the function.


def my_function(food):
    print(type(food))
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]  # list
food = {"meat", "chicken"}  # set
lunch = {"starter": "kebab", "maincourse": "biryani"}  # dictionary
my_function(fruits)
my_function(food)
my_function(lunch)


# Return Values:
# to let a function return a value, use the return statement:

def my_function(x):
    return 5 * x


print(my_function(3))


def SumOdd(nums):
    sum = 0
    rnum = []
    for x in nums:
        if x % 2 != 0:
            rnum.append(x)
            sum += x
    return sum


print(SumOdd([1, 2, 3, 4, 5, 6]))


# Recursion
# function which calls itself

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(2))
