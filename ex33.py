# While loops
# This script introduces while-loops. The code will keep running until the block is False
i = 0
numbers = []

while i < 6: # while loop runs until the expression is False
    print "At the top of i is %d" % i
    numbers.append(i) # this inserts the contents of i to the numbers list [0]

    i = i + 1 # adding 1 to i until the block becomes False
    print "Numbers now: ", numbers # printing the contens of i as a list [0, 1]
    print "At the bottom i is %d" % i


print "The numbers: " # this wont print until the block above becomes False.

for num in numbers: # prints the numbers after the last print statement.
    print num
