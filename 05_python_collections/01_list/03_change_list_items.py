# Change item Value
# To change the value of a specific item, refer to the index number:

thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

# Change a range of item value
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList)

# if inserted more items than you replace, the new items will be inserted where you specified,and the remaining items will move accordingly.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print(len(thislist))

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thisList = ["apple", "banana", "cherry", "banana"]
thisList[1:3] = ["watermelon"]
print(thisList)

# using insert() method
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "watermelon")
print(thisList)
