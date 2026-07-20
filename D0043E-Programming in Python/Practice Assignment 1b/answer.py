# Import the math module
import math

# Create variables
'''
distance_km: Total distance of the trip in kilometers with 450 km
fuel_efficiency: The car's fuel efficiency
in kilometers per liter with 15 km/l.
fuel_price: The price of fuel per liter with $1.20 per liter.
average_speed: The car’s average speed in kilometers per hour with 80 km/h.
'''
distance_km = 450
fuel_efficiency = 15
fuel_price = 1.20
average_speed = 80

# Calculate BMI
'''
Calculate the total travel time (in hours):
Round up the travel time to the nearest hour.
'''
time = math.ceil(distance_km / average_speed)
fuel_needed = distance_km / fuel_efficiency
fuel_cost = fuel_needed * fuel_price


# Display the result on screen
'''
Print the following details in a clear and structured format:
Total Distance: 450 km
Estimated Travel Time: 6 hours
Fuel Needed: 30.00 liters
Total Fuel Cost: $36.00
'''

print(f"Total distance: {distance_km} km")
print(f"Estimated travel time: {time} hours")
print(f"Fuel needed: {fuel_needed: .2f} liters")
print(f"Total fuel cost: ${fuel_cost: .2f}")
