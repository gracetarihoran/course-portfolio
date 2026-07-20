# Variables for rectangle
length = float(input("Enter the length "))
width = float(input("Enter the width "))


# Function for calculating rectangle area
def rectangle_area(_length, _width):
    area = _length * _width
    return area


# Variables for circle
PI = 3.14
radius = float(input("Enter the radius "))


def circle_area(_radius):
    area = PI * (_radius ** 2)
    return area


# Calculate and print the rectangle's area
result1 = rectangle_area(length, width)
print(f"The area of the rectangle is: {result1}")

# Calculate and print the circle's area
result2 = circle_area(radius)
print(f"The area of the circle is: {result2}")
