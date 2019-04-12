#--- assert: (ensure) that something is true ----

assert "hey" == "hey" # no problem
assert True == True # everything is fine
assert 1 + 10 == 11 # nothing to see here

assert True == False #-- creates an AssertionError --
