# Loop Through a tuple
# you can loop through the tuples using the following
# for loop:
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)
print("_____________________________________")
# range through index
thisTuple = ("apple", "banana", "cherry")
for i in range(len(thisTuple)):
    print(thisTuple[i])

print("_____________________________________")

# Using While Loop
thisTuple = ("apple", "banana", "cherry")
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i = i + 1
