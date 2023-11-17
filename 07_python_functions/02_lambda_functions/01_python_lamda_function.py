# Python Lambda
# A lamda function is a small anonymous function
# syntax <lambda arguments : expression>
# expression is executed and the result is returned

x = lambda a : a+10
print(x(65))

# lambda function can take any number of arguments.
x = lambda a, b, c:  a + b + c
print(x(5, 6, 2))

x = lambda a,b,c: a*b*c
print(x(2,3,4))

# Why use lambda function?
# power of lambda is better shown when you see them as an anonymous function inside another function.

def my_func(n):
    return lambda a: a*n
doubler = my_func(2)
print(type(doubler))
print(doubler(11))

def my_func(n):
    return lambda a: a*n
tripler = my_func(3)
print(tripler(11))


def my_func(n):
     return lambda a:a*n

doubler = my_func(2)
tripler = my_func(3)
fourth = my_func(4)

print(doubler(11))
print(tripler(11))
print(fourth(11))


def palindrome(str):
    str = str.lower()
    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

print(palindrome("radar"))    