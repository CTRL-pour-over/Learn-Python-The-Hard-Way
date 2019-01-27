#This script quizzes you on ordinal and cardinal numbers and tries get you to understand the differences
#The script will ask you to type an animal at a given coordinate within a list and you must guess which animal that is.
# Side note: I know theres a simpler way of doing this :(

print "\nThis is a ordinal / cardinal counting quiz.\n\nTry and get what position our animals are in the list! GOOD LUCK!\n"
print "\n\n\nHere is the list: \nanimals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']\n"

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

#the animal at 1 is the 2nd animal and is a python
#the 2nd animal is at 1 and is a python
guess1 = raw_input("The animal at 1: -> ") # Cardinal
print "Your guess is %s." % guess1
print "The answer is %s.\n" % (animals[1])

#the third animal is at 2 and is a peacock
#the animal at 2 is the third animal and is a peacock
guess2 = raw_input("The third (3rd) animal: -> ") # Ordinal
print "Your guess is %s." % guess2
print "The answer is %s.\n" % (animals[2])

#the first animal is at 0 and is a bear
#the animal at 0 is the 1st animal and is a bear
guess3 = raw_input("The first (1st) animal: -> ") # Ordinal
print "Your guess is %s." % guess3
print "The answer is %s.\n" % (animals[0])

#the animal at 3 is the 4th animal and is a kangaroo
#the 4th animal is at 3 and is a kangaroo
guess4 = raw_input("The animal at 3: -> ") # Cardinal
print "Your guess is %s." % guess4
print "The answer is %s.\n" % (animals[3])

print """Printing the list again:
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']\n"""

#the fifth animal is at 4 and is a whale
#the animal at 4 is the 5th animal and is a whale
guess5 = raw_input("The (5th) animal: -> ") # Ordinal
print "Your guess is %s." % guess5
print "The answer is %s.\n" % (animals[4])

#the animal at 2 is the 3rd animal and is a peacock
#the 3rd animal is at 2 and is a peacock
guess6 = raw_input("The animal at 2: -> ") # Cardinal
print "Your guess is %s." % guess6
print "The answer is %s.\n" % (animals[2])

#the sixth animal is at 5 and is a platypus
#the animal at 5 is the 6th animal and is a platypus
guess7 = raw_input("The sixth (6th) animal: -> ") # Ordinal
print "Your guess is %s." % guess7
print "The answer is %s.\n" % (animals[5])

#the animal at 4 is the 5th animal and is a whale
#the 5th animal is at 4 and is a whale
guess8 = raw_input("The animal at 4: -> ") # Cardinal
print "Your guess is %s." % guess8
print "The answer is %s.\n" % (animals[4])
