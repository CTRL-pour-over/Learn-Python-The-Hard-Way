# The if statements, used in conjunction with the > , < operators will print
# the following text if True.
# In other words, ( if x is True: print "a short story" )
# Indentation is needed for syntax purpouses. if you do not indent you will get
# "IndentationError: expected an indented block".
# If you do not create a colon after the new block of code is declared,
# you will get a SyntaxError: invalid syntax.

people = 20
cats = 30
dogs = 15


if people < cats and 1 == 1: # Prints first
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs and "test" != "testing": # Prints second
    print "The world is dry!"


dogs += 5 # "increment by" operator. This is the same as 15 + 5 = 20

if people >= dogs: # Prints third
    print "People are greater than or equal to dogs."

if people <= dogs: # Prints fourth
    print "People are less than or equal to dogs."


if (not people != dogs): # Prints fifth
    print "People are dogs."
