# Import the math module
import math

# Function to calculate travel time


def calculate_travel_time(distance_km, average_speed):
    travel_time = math.ceil(distance_km / average_speed)
    return travel_time


# Function to calculate fuel needed that returns the total fuel required
def calculate_fuel_needed(distance_km, fuel_efficiency):
    fuel_needed = distance_km / fuel_efficiency
    return fuel_needed


# Function to calculate fuel cost that returns the total fuel cost
def calculate_fuel_cost(fuel_needed, fuel_price):
    fuel_cost = fuel_needed * fuel_price
    return fuel_cost


# Create variables
distance_km = int(input("Enter the distance: "))
fuel_efficiency = int(input("Enter the fuel efficiency: "))
fuel_price = float(input("Enter the fuel price: "))
average_speed = int(input("Enter the average speed: "))


# Calculate time, fuel, and fuel cost
hours = calculate_travel_time(distance_km, average_speed)
liters = calculate_fuel_needed(distance_km, fuel_efficiency)
cost = calculate_fuel_cost(liters, fuel_price)

# Display the result on screen
print(f"Total Distance: {distance_km} km")
print(f"Estimated Travel Time: {hours} hours")
print(f"Fuel Needed: {liters: .2f} liters")
print(f"Total Fuel Cost: ${cost: .2f}")
