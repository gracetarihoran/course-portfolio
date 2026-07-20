def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    result = 0
    negative = False

    if num2 < 0:
        num2 = -num2
        negative = True

    for i in range(num2):
        result = result + num1

    if negative:
        return -result
    return result


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = add(a, b)
elif operation == '-':
    result = subtract(a, b)
elif operation == '*':
    result = multiply(a, b)
elif operation == '/':
    result = divide(a, b)
else:
    result = "Error"

if result == "Error":
    print("Invalid operation!")
else:
    print(f"The result of {a} {operation} {b} is {result}")
