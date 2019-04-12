#--- for: loop over a collection of things ----
love = ['<3']

for thing in love:
    print "\tthats so sweet" * 100
    print "this is a test"
    truth = raw_input("tell me you love me")
    if truth != "i do":
        print "\ti hate you" * 100000000
