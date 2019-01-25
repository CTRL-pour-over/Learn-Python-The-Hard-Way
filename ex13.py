# Parameters, Unpacking, Variables

# line 2 is where we import argv
from sys import argv
# here is where we unpack our modules
# in order to make ex13 run, we have to provide the terminal with 3 arguments upon running the script.
script, first, second, third = argv
# lines 7 - 10 is where we output code to the terminal
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
