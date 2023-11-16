# Import from module
# we can choose to import parts from the module, using <from> keyword.

import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from _a02_variables_in_module.python_variable_module1 import MyList
from _a01_create_a_module.python_create_function_modules import greetingInCaps

print(MyList)
greetingInCaps("make me capital letter")