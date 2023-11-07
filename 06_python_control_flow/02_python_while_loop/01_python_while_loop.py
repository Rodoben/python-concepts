# Python while loop
# with while loop we can execute a set of statements as long as a condition is true.
# while loop requires relevant variables to be ready, i.e variable i set to 1.

i = 1
while i < 6:
    print(i)
    i += 1

# The Break statement  <break>
# with break statement we can stop the loop even if the while condition is true.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("________________")
# Continue Statement
# with continue statement we can stop the current iteration,and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement
# with else statement we can run a block of code once when the condition is no longer true.
print("________________")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
