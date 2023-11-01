# integer

import random
x = 1
y = 661313213546531313213
z = -25454542
print(x, "------", type(x))
print(y, "------", type(y))
print(z, "------", type(z))
print("------------------------------------")
# float

x = 1.3
y = 661313213546531313213.36
z = -25454542.36
print(x, "------", type(x))
print(y, "------", type(y))
print(z, "------", type(z))

print("------------------------------------")
# complex

x = 35e3j
y = 12E4j
z = -87.7e100j
print(x, "------", type(x))
print(y, "------", type(y))
print(z, "------", type(z))
print("------------------------------------")


# Type conversion
x = 1
y = 2.6
z = 1j


a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# random numbers
print(random.randrange(1, 10))
print(random.randrange(1, 10))
