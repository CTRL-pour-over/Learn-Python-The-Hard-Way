# This script takes a given file and re-writes it. Careful!
from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that. hit RETURN."

raw_input("?")
# the 'w' perameter on line 12 allows us to open the file in write mode.
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# target.truncate() will wipe the file
target.truncate()

print "Now I'm going to ask you for three lines."
# line1, line2, line3 is where we're gonna store our replacement data
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
# here we are writing line1, line2, line3 data into the truncated file.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# below is how we close the file.
print "And finally, we close it."
target.close()
