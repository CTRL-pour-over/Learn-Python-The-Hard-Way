# While loops
# This script introduces while-loops. The code will keep running until the block is False
#The study drills ask first to recreate the while loop as a function() and then again as a for-loop
#thus the commented out blocks of code. Need to figure out a method to organize scripts like this.

# i = 0
# numbers = []

# while i < 6: # while loop runs until the expression is False
    # print "At the top of i is %d" % i
    # numbers.append(i) # this inserts the contents of i to the numbers list [0]

    # i = i + 1 # adding 1 to i until the block becomes False
    # print "Numbers now: ", numbers # printing the contens of i as a list [0, 1]
    # print "At the bottom i is %d" % i


# print "The numbers: " # this wont print until the block above becomes False.

# for num in numbers: # prints the numbers after the last print statement.
    # print num


#This study drill asks that we re-create the while-loop design using only a function()
def buildList(num):
    numList = []
    i = 0
    while i < num:
        numList.append(i)
        i += 1
        print "i: %d, " % i,
        print "list: ", numList
    #note: you don't need to return a value

#you can hard code any number here, of course
buildList(6)


#This study drill asks to re-create the while-loop using a for-loop and range()
#i = 0
#list = []
#print "This is before the loop"
#for i in range(6):
#    print("Here are the numbers: %d") % i
#    print "this is the end of the loop"

#print "this is a new block of code, signifying the end of the script. Have a nice day."
