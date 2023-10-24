x = "awesome"

def myfunc():
    print("Python is "+ x)

myfunc()    


def myfunc2():
    x = "fantastic"
    print("Python is "+x)

myfunc2()    

print("Python is " + x)

# global keyword is used to declare variable globally.
def myfunc3():
    global x 
    x = "ronald"
myfunc3()

print("Python is "+ x)