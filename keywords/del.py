#--- del: Delete from dictionary. ----
x = ["apple", "banana", "cherry"]

print "this is the list: %r" % x

choice = raw_input("delete [0] from the list? y / n >>>  ")

if choice == 'y':
    print "Here is the list now."
    del x[0]
else:
        print "okay... Here is the list."
print(x)
