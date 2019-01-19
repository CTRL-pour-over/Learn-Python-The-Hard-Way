# call function() and insert parameters for (a, b)
def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b
# call function() and insert parameters for (a, b)
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
# call function() and insert parameters for (a, b)
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
# call function() and insert parameters for (a, b)
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "LEt's do some math with just functions!"
# here we are giving our parameters for our functions. EZ
v1 = float(raw_input("Let's ADD two numbers --> "))
v2 = float(raw_input("Now type the second number --> "))
age = add(v1, v2)

h1 = float(raw_input("Let's subtract two numbers --> "))
h2 = float(raw_input("Now type the second number --> "))
height = subtract(h1, h2)

w1 = float(raw_input("Let's multiple two numbers --> "))
w2 = float(raw_input("Now type the second number -->"))
weight = multiply(w1, w2)

iq1 = float(raw_input("Let's divide two numbers --> "))
iq2 = float(raw_input("Now type the second number --> "))
iq = divide(iq1, iq2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# (iq / 2 = 25), (weight * iq = 4500) (height - 4500 = -4426) (age + -4426 = -4391)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
