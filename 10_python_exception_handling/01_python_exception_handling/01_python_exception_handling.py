# Python exception handling.
  # try -> block lets you test a block of code for error
  # except -> block lets you handle the error
  # else -> block helps to execute a block of code when no error.
  # finally -> lets you execute the code regardless of the try and except block.

# Exception handling.
  # when error happens the python will normally stop its execution and provide error message.
  # these exception can be handled using try statement.

# x = 9
try:
  print(x) # since x is not initialized, it will throw an error.
except:  #  except keyword allows to handle the error.
  print("An Exception occured!")  # hence this line will be executed.

# Many Exception
  # we can define many exception block. if we want to execute a special block of code for special kind of error.
  # other type of error are FileNotFoundError, ZeroDivisionError, ValueError, TypeError, SyntaxError.

# NameError
try:
  print(x)
except NameError:
  print("Variable is not defined")
except:
  print("something else went wrong")  
    
# SyntaxError
try:
  x = 10 / 0
  print(x)
except SyntaxError:
   print("Syntax error infinity")
except:
  print("Something else went wrong")     

# TypeError
try:
  x = "string"+10
except TypeError:
   print("TypeError: cannot add two different types")
except:
   print("Something else went wrong")     

#ValueError
try:
  x = int("abc") 
except ValueError:
   print("ValueError: cannot convert it to the specific datatype")
except:
   print("Something else went wrong")  

#ZeroDivisionError
try:
  x = 10 / 0
except ZeroDivisionError:
   print("ZeroDivisionError: cannot divide by 0")
except:
   print("Something else went wrong")  
         
# FileNotFoundError
try:
  with open("nonexist.txt","r") as file:
    content = file.read()
except FileNotFoundError:
  print("FileNotFound: file is not present")             


# Else
  # we can use else keyword to define a block of code to be executed if no errors were raised.

try:
  print("Hello")
except:
  print("Something Went Wrong")
else:
  print("Nothing Went Wrong")  

# Finally
  # if finally block is specified, it will be executed regardless of try block raises an error or not.
try:
  print(x)
except:
  print("Variable not defined")
else:
   print("There was no error")
finally:
   print("I am out of the try except block")        

   # finally block will be useful to close objects or clean up resources.

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum ipsum ronald")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")            


# Raise an exception
# to throw or raise an exception, use the <raise> keyword.

x = -1
if x < 0:
  raise Exception("Sorry a number cannot be below Zero.")





