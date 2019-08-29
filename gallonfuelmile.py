"""
Write a program that prompts the capacity, in gallons, of an automobile fuel
tank and the miles per gallons the automobile can be driven. The program
outputs the number of miles the automobile can be driven without refueling.
"""

# this problem is almost like speed calculation problem
# fuel = time, miles = distance, speed = distance / fuel
# here the fuel and the miles travelled is in a direct proportion

# fuel capacity in gallons
print('..Fuel is measured in gallons..')
fuelcapacity = float(input('Enter the fuel capacity: '))

# miles that the vehicle can travel per gallon
milespergallons = float(input('Enter the miles travelled per gallon: '))

# the number of miles the automobile can be driven without refueling
numberofmiles = fuelcapacity * milespergallons

print('The automobile can be driven without refueling for', numberofmiles,
 'miles travelled')
