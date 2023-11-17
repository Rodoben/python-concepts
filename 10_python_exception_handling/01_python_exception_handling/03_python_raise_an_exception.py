# raise Exception as TypeError:
x = "hello"
if not type(x) is int:
   raise TypeError("Only integer allowed")