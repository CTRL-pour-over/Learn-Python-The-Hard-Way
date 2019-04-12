# --- is operator: like == to test equality ----
# --- The is operator does not match the values of the variables, but the instances themselves.----
# --- It tests if two variables point the same object, not if two variables have the same value.----
print 1 is 1
print 1 is 2

love = raw_input("say you love me >>>   ")
list = ['i love you', '<3', 'i do']

for thing in list:
    if thing in love:
        list = love
        if list is love:
            print "i love you so much bb " * 9999
    if list is not love:
        print "i hate you " * 9999
