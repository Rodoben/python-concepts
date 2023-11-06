# Python - Loop sets
# we canloop through a set using for keyword
# its ranges over the set randomly,hence it is unordered and unindexed.
thisList = {"apple", "mrinalini", "ronald"}
for x in thisList:
    print(x)

print("__________________")
thatList = set(("apple", "mrinalini", "ronald"))  # using constructor set(())
for x in thatList:
    print(x)
