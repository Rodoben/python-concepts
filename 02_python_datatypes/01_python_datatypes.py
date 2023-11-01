# in python data type is set when you assign a value to a variable.

x = "Hello World"
print(x, "----", type(x))  # string

x = 20
print(x, "----", type(x))  # int

x = 20.5
print(x, "----", type(x))  # float

x = 1j
print(x, "----", type(x))  # complex

x = ["apple", "banana", "kela"]
print(x, "----", type(x))  # list []

x = ("apple", "banana", "kela")
print(x, "----", type(x))  # tuple()

x = range(6)
print(x, "----", type(x))  # range

x = {"name": "John", "age": 36}
print(x, "----", type(x))  # dict

x = {"apple", "banana", "cherry"}
print(x, "----", type(x))  # set {}

x = frozenset({"apple", "banana", "cherry"})
print(x, "----", type(x))  # frozenset

x = True
print(x, "----", type(x))  # bool

x = b"Hello"
print(x, "----", type(x))  # bytes

x = bytearray(5)
print(x, "----", type(x))  # bytearray

x = memoryview(bytes(5))
print(x, "----", type(x))  # memoryview

x = None
print(x, "----", type(x))  # None
