# Prompting and Passing

from sys import argv
# you have to give a user_name argument when trying to run the program
# script saved ex14.py from when we typed it into the terminal for later use in text.
script, user_name = argv
# this is a simple prompt that will put an > whenever the user gets to type.
prompt = '> '
# here is where the script prints out the two arguments we provided in order to run the script.
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# saving more variables here (likes, lives, computer)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)
# below is where we output all the data we've gathered.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
