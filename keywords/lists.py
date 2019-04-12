# lists: stores a list of things #
i = []
i = raw_input("Give me some words to put in the list. >>  ")
print "Here's what you said: %s" % i

rp = raw_input("could you repeat that? >>  ")
if rp == i:
    print "correct"
else:
    print "false"
