# this is our main function. everything in the script will run through this eventually
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# here we insert the cheese_count & boxes_of_crackers directly as numbers (20, 30)
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# here we actually save numbers to the variables. more on line 17.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # see that?

# line 21 we're adding numbers inside the function. so we'll have 30 cheeses and 11 boxes
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# amount_of_cheese = 10 ^^^
# amount_of_crackers = 50 ^^^
# below we are actually adding numbers to those already existing variables.
# this means we will have 110 cheeses and 1050 boxes of crackers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
