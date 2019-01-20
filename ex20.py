from sys import argv

script, input_file = argv
# lines 5 / 6 is our print all function
def print_all(f):
    print f.read()
# lines 8 / 9 is the function that rewinds via seek.(0)
def rewind(f):
    f.seek(0)
# here is our line printing function
def print_a_line(line_count, f):
    print line_count, f.readline()
# line 14 saves our opened input_file as the current_file variable
current_file = open(input_file)

print "First let's print the whole file:\n"
# line 18 runs our already opened input_file, saved as current_file, thru the print_all function.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# line 22 runs current_file thru the rewind function on lines 8 / 9
rewind(current_file)

print "Let's print three lines:"
# NEW VARIABLE ALERT BELOW (current_line)
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Current line = seek(0) + 1 each time. this stacks so that we
# can find lines 1, 2 and 3.
