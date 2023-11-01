# 1 capitalize()	Converts the first character to upper case
x = "ronald benjamin"
print(x.capitalize())

# 2 casefold()	Converts string into lower case
x = "Ronald Benjamin"
print(x.casefold())

# 3 center()	Returns a centered string
x = "Ronald Benjamin "
print(x.center(30))

# 4 count()  	Returns the number of times a specified value occurs in a string
x = "Ronald Benjamin"
print(x.count("a"))

# 5 encode()	Returns an encoded version of the string
x = "Ronald Benjamin"
print(x.encode())

# 6 endsWith() Returns true if the string ends with the specified value

x = "Ronald Benjamin"
print(x.endswith("in"))

# 7 expandtabs() Sets the tab size of the string
x = "Ron\tald Be\tnjam\tin"
print(x)
print(x.expandtabs(5))

# 8 find() searches a string for a specified value returns the position
x = "Ronald Benjamin"
print(x.find("min"))

# 9 format() formats the specified value value in a string
x = "Ronald Benjamin age is {0}"
age = 36
print(x.format(age))

# 10 format_map() formats the specified value in a string
x = {'name': 'ronald', 'lastname': 'Doe'}
age = 36
print('{name} {lastname}'.format_map(x))
