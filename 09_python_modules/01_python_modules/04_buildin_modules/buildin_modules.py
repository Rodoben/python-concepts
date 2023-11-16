# Python Modules
# There are several built-in modules in python which we can use using <import> keyword.
# to make an import from another directory its name should start from _ followed by an alphabet or alphabet itself
import platform
import sys
import os

x= platform.system()
print(x)

#dir() function -> to list all the function names in a module.

x = dir(platform)
print(x)

# To import from another directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from _a01_create_a_module import python_create_function_modules as vm
from _a02_variables_in_module import python_variable_module1 as vv
vm.greeting("ronald")
vm.greetingInCaps("ronald")

x = vv.myDict
print(x)
x = vv.MyList
print(x)