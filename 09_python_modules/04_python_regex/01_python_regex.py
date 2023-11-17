# Python RegEx
# A RegEx or Regular expression is a sequence of character that forms a search pattern.
# Regex can be used to check if a string contains the specified search pattern.

# python has built-in package called <re>, which can be used to work with regular expression.

import re

txt = "The rain in Spain"
x = re.search("^The .*Spain$",txt)
print(x)
if x:
    print("Yes!, we have a match")
else:
    print("No Match")    