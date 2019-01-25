# Strings and Text
# This script demonstrates the function of %s, %r operators. 

x = "There are %d types of people." % 10
binary = "binary" # saves the string as a variable
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # inserting variables ()
# here's where we print out our variables ^^^
print x
print y
print "I said: %r." % x # prints
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# % hilarious becomes the missing variable for joke_evaluation
print joke_evaluation % hilarious
# more assigning strings to variables. will be used later
w = "This is the left side of..."
e = "a string with a right side"
# below is where we print the obove variables (w, e)
print w + e
