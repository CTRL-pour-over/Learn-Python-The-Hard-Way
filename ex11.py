print "How old are you?",
# raw_input() allows the end user to input words or letters.
# here we collect the age variable from the user. We'll spit that out later
age = raw_input()

print "How tall are you?",
# collecting the height data from the user
height = raw_input()

print "How much do you weight?",
# collecting the weight variable from the user.
weight = raw_input()
# the %r is called a "string formatting operation".
# %s is the str function, %r is the repr function. (readmore)
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight) # this  is how we insert our data into the string
