#--- try: Try this block, and if exception, go to except.----
while True:
     try:
         x = int(raw_input("Please enter a number: "))
         break
     except ValueError: # if the user fails to enter a number
         print "Oops!  That was no valid number.  Try again..."
