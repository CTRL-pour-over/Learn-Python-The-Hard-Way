# Variables And Names
# This script saves a numeric value to a variable.
# Then is does math with just the variables using their numeric values.
# It also prints the numeric values in the same lines as print statements
# This is done by placing a comma after a string, then after the variable, before the next string.
cars = 100
# floating point numbers (4.0) allow fractional outcomes
space_in_a_car = 4.0
drivers = 30
passengers = 90
# 100 - 30
cars_not_driven = cars - drivers
# 30
cars_driven = drivers
# 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
# 90 / 30
average_passengers_per_car = passengers / cars_driven

# insert a comma after a string before variable and after variable
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
