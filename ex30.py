# Else and If

# This script introduces else and if statements
# The output will only work with a true statement
# elif is like an alternative option, only outputting if it is True

# Here are our variables.
people = 30
cars = 40
trucks = 15

# we can insert boolean logic to these if statements to add alternative solutions.
if cars > people or trucks < cars: # This is True or True
    print "We should take the cars." # This is the only line that will print in this block.
elif cars < people: # False
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars: # False
    print "That's too many trucks."
# if trucks > cars is not True, try elif trucks < cars: else print "maybe we shouldnt"
elif trucks < cars: # This is True
    print "Maybe we could take the trucks." # This line will print from this block.
# if both arguments above are False, continue with else:
else:
    print "We still can't decide."
# if the argument is True: print the following.
if people > trucks: # This is True
    print "Alright, let's just take the trucks." # This will be the output line.
# else: is printed if the if statement is False.
else:
    print "Fine, let's stay home then."
