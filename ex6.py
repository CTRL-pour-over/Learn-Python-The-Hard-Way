# the x = makes line 2 only print out on line 7 (print x)
x = "There are %d types of people." % 10
binary = "binary" # saves the string as a variable
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # inserting variables ()
# here's where we print out our variables ^^^
print x
print y
# line 10 we print x aka (line2) again.
print "I said: %r." % x
print "I also said: '%s'." % y
# line 13 we program a variable to be False
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# line 16 ( % hilarious ) is where gets inputted into line 14's %r
print joke_evaluation % hilarious
# more assigning strings to variables. will be used on line 21
w = "This is the left side of..."
e = "a string with a right side"
# below is where we print the obove variables (w, e)
print w + e
