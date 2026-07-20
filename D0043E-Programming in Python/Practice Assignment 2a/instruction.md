#### Mini-Project: Rectangle and Circle Area Calculations with Input and Functions

**Learning Goals**

*   Practice using the `input()` function to get user input.
*   Understand how to create and call functions in Python.
*   Apply formulas for basic geometric area calculations.
*   Practice writing Python scripts and outputting results in a formatted string.

**Task**

1.  In a file named `answer.py` complete the following tasks.
    
2.  **Rectangle Area Calculation**
    
    *   Write a function named `rectangle_area(length, width)` that takes two arguments and returns the area of a rectangle using the formula:
        
            area = length * width
        
    *   Use `input()` to ask the user to enter the `length` and the `width` of the rectangle.
        
        > 💡 Remember: values from `input()` come as strings, so convert them to numbers with `int()` or `float()`.
        
    *   Call your `rectangle_area` function with the user-provided values.
    *   Print the result in the exact format:
        
            The area of the rectangle is: [result]
        
3.  **Circle Area Calculation**
    
    *   Write a function named `circle_area(radius)` that takes the radius as an argument and returns the area of a circle using the formula:
        
            area = PI * (radius ** 2)
        
        Use `PI = 3.14`.
    *   Use `input()` to ask the user to enter the radius of the circle.
    *   Call your `circle_area` function with the user-provided value.
    *   Print the result in the exact format:
        
            The area of the circle is: [result]