#--- Continue: Don't process more of the loop, do it again ----
#--- alters the flow of a loop ----
for letter in 'Python':     # First Example
   if letter == 'h':
      continue # output skips 'h'
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue # output skips 5
   print 'Current variable value :', var
print "Good bye!"
