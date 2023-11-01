# strings in python are surrounded by either single or double quotation marks.
print("Hello")
print('Hello')

# assign string to a variable
x = "Ronald Benjamin"
print(x)
print("__________________________________")
# MultiLine String """---""" or '''---'''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("__________________________________")
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("__________________________________")

# strings are arrays
a = "Hello, World!"
print(a[0])
print("__________________________________")
# Looping through a string
for x in "ronald":
    print(x)
# String length
print("__________________________________")
a = "hello World"
print(len(a))

# Check string length
# to check a certain phase or character is present in a string, we can use <in>
txt = "The best things in life are free!"
print("free" in txt)
print("__________________________________")

# Check string is present using <if condition> <not in>
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check string is present using <if NOT condition> <not in>
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")
