#---global: Declare that you want a global variable.----
#--- a global variable can be summoned at any point in the script. ----
x = "global variable"

def babygurl():
    print "x inside : %s" % x

babygurl()
print "x outside: %s" % x
