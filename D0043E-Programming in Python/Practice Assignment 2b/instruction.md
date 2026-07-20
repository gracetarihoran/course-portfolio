#### Mini-Project: Trip Planner with Input and Functions

**Learning Goals**

*   Practice using the `input()` function to get user input.
*   Learn how to create and call functions in Python.
*   Use the `math` module for real-world calculations.
*   Apply arithmetic operations to solve practical problems like travel time and costs.
*   Combine multiple calculations in a structured program.

**Task**

1.  In a file named `answer.py` write a Python program to calculate travel costs and time for a road trip.
    
2.  **Functions:**
    
    *   Write a function `calculate_travel_time(distance_km, average_speed)` that returns the travel time in hours, **rounded up** to the nearest whole hour. Use `math.ceil()`.
    *   Write a function `calculate_fuel_needed(distance_km, fuel_efficiency)` that returns the total fuel required.
    *   Write a function `calculate_fuel_cost(fuel_needed, fuel_price)` that returns the total fuel cost.
3.  **Get User Input:**
    
    *   Ask the user to enter the `distance_km`, `fuel_efficiency`, `fuel_price`, and `average_speed`.
    *   Convert the inputs to numbers using `float()`.
4.  **Perform Calculations:**
    
    *   Call your functions to calculate the travel time, fuel needed, and fuel cost.
5.  **Display Results:**
    
    *   Print the results in the exact format below (with the correct values depending on user input):
        
            Total Distance: [distance] kmEstimated Travel Time: [hours] hoursFuel Needed: [liters] litersTotal Fuel Cost: $[cost]
        

**Example Run (using distance=450, fuel\_efficiency=15, fuel\_price=1.20, average\_speed=80):**