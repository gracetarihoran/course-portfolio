def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


choice = " "
while choice not in "CF":
    choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ")
    choice = choice.strip()
    choice = choice.upper()

temp_str = input("Enter the temperature: ")
temp = float(temp_str)


if choice == "C":
    converted = celsius_to_fahrenheit(temp)
    print(f"{temp: .1f}°C is {converted: .2f}°F")
else:   # choice == "F"
    converted = fahrenheit_to_celsius(temp)
    print(f"{temp: .1f}°F is {converted: .2f}°C")
