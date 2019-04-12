#---if : if condition ----
choice = raw_input("left or right--->>>   ")

condition = True

while condition is True:
    if choice == "left":
        print "you are now inside the left room."
    elif choice == "right":
        print "you are now inside of the right room"
    else:
        print "don't play games with me."
