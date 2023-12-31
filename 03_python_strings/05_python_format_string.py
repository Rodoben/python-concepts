# string format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
####################################
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
####################################
# But we can combine strings and numbers by using the format() method!
# format()- methos takes the passed arguments, formats them, and places them in the string where the placeholder {} are:

age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

# without index
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# with indexing
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
