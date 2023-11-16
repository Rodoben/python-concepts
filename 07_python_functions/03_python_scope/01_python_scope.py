# Python Scope

# A variable is only available from inside region it is created. This is called scope.

#Local Scope
# A Variable created inside a function belongs to the local scope of that function,can be used inside that function.

def myfunc():
    x = 300
    print(x)
myfunc()    

# print(x) outside of function block or scope

# Function inside a function
# variable defined is not available outside the function but is available for any function inside a function

def myfunc():
    x = 400
    def innerFunction():
        print(x+200) # scope of variable x is available here.
    innerFunction()
    print(x)
myfunc()



# GLobal Scope
# variable created in the main body of the python code is a global varibale, belongs to global scope
# Global variable are available within any scope, global and local

x = 500 # varibale declared globally
def myfunc():
    print(x)

myfunc() 
print(x) # also avaiable outside the function body since globally initialized.


# Naming Variable
# if operated with same variable name inside and outside of a function, pyhton treats them as two separate variables, one available in the global scope(outside function) and one in the local scope(function)
print("__________")
x = 190
def func1():
    x = 200
    print(x)
func1()
print(x)

# Global Keyword
# if needed to creatre a global variable, but stuck in local scope, use global keyword.
# keyword <global> makes the varibale global

def myfunc():
    global x  # global keyword used to make the varibal x global
    x = 300
    print(x)
myfunc()    
print(x)

# we cna use global keyword if you want to make a change to a global variable inside a function.

x = 300

def myfunc():
    global x
    x =200
myfunc()
print(x)    
