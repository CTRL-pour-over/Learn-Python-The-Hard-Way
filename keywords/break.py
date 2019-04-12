#--- break: alters the flow of a loop ----
#--- The break statement, like in C, breaks out of the innermost enclosing for or while loop.----
#--- this is a control flow tool ----
list = ['thomas']
choice = raw_input("what is your name")
for thing in list:
    if thing in choice:
        print "nice to meet you"
    else:
        print "boutta break bruh"
        break
