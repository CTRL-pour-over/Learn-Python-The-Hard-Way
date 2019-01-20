# this file is designed to open and read a given file as plain text
# provide ex15.py with an argument (file) and it will read it to you
# then it will as for the filename again, you can also give it a different file.
from sys import argv
# here is how we can give an additional argument when trying to run the script (insert read file)
script, filename = argv
# line 8 doesnt actually open the file to the user. this is under the hood.
txt = open(filename)
# line 11 is how we actually read the file to the user. but first you must open it.
print "Here's your file %r:" % filename
print txt.read()
# here is where we ask for the filename again and assign it to a variable (file_again)
print "Type the filename again:"
file_again = raw_input("> ")
# here is how we open the new file in the directory
txt_again = open(file_again)
# here is how we actually print or read() the second file txt_again.read()
print txt_again.read()
