# Loop through a list
# you can loop through the list using a for loop:

thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

# looping through the list items by referring to their index number
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(i)
    print(thisList[i])
print("_______________________________")
# looping using while loop
thisList = ["apple", "banana", "cherry"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i+1
print("_______________________________")
# Looping using list Comprehension
thisList = ["apple", "banana", "cherry"]
[print(x) for x in thisList]
