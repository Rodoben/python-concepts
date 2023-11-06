# Unpacking a Tuple
# when we create a tuple, we normally assign values to it, this is called packing a tuple.

fruits = ("apple", "banana", "grapes")  # packing a tuple
print(fruits)

(green, yellow, red) = fruits  # unpacking a tuple
print(green)
print(yellow)
print(red)

# Using Asterisk *
# if the number of variable is less, we can use * to varibale name, and rest value is stored as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
