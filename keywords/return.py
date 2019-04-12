# --- return: Exit the function with a return value----
def foo():
    print "hello from inside of foo"
    return 1

foo() # this only produces the print statement in the function
print "this is in between foo() and print foo()\n"
print foo() # this produces the print statement and returns 1
