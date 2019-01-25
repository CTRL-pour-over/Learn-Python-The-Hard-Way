# Printing, Printing

# line 2 %r allows for future input
formatter = "%r %r %r %r"
# line 4 prints 1 2 3 4
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") # will print the strings in the ( )
print formatter % (formatter, formatter, formatter, formatter) # prints %r %r %r %r (4 times)
# below me will print out the strings not in a row, but side by side
print formatter % (
    "I had this thing." ,
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
