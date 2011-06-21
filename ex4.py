# Number of cars
cars = 100
# Amount of space in a car
# used floating point decimal for accuracy
space_in_a_car = 4.0
# Number of drivers 
drivers = 30
# Number of passengers
passengers = 90
# Calculation of the number of cars without drivers
cars_not_driven = cars - drivers
# A driver for each car
cars_driven = drivers
# Carpool Capacity number
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"
