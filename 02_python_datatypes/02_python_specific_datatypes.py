x = str("Hello world")
print(x, "___", type(x))

x = int(23)
print(x, "___", type(x))

x = float(20.3)
print(x, "___", type(x))

x = complex(20j)
print(x, "___", type(x))

x = list(["apple", "banana", "banana"])
print(x, "___", type(x))

x = tuple(("apple", "banana", "banana"))
print(x, "___", type(x))

x = set(("apple", "banana", "banana"))  # make sure ()
print(x, "___", type(x))

x = dict(name="ronald", age=12)  # make sure of = when ()
print(x, "___", type(x))

# frozenset can be done using both () and {}
x = frozenset(("apple", "banana", "banana"))
print(x, "___", type(x))

x = bool(5)
print(x, "___", type(x))

x = bytes(5)
print(x, "___", type(x))

x = memoryview(bytes(5))
print(x, "___", type(x))

x = bytearray(5)
print(x, "___", type(x))
