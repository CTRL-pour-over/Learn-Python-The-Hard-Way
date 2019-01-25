# More Files

# This script copys text from one file to another (from_file, to_file)
from sys import argv
from os.path import exists

script, from_file, to_file = argv
# line 7 is the first bit out ouput text in this script.
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# # in_file = open(from_file) POOR CODE # #
# # indata = in_file.read() POOR CODE # # LINE 12 FOR THE SINGLE LINE FIX.
in_file = open(from_file); indata = in_file.read() # << optimization at its finest.
in_file = open(from_file)
# second but of output text len() tells you how many bytes are in a file.
print "The input file is %d bytes long" % len(indata)
# line 17 gives a True of False statement depending on if the output file exists.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
# line 21 we open the out_file in write mode. Then we write(indata) to fill the file.
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."
# closing the files after our work is finished.
out_file.close()
in_file.close()
