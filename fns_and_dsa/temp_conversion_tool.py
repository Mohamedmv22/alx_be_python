FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{fahrenheit}°F is {celsius}°C")


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")


temperature_input = input("Enter the temperature to convert:")
if temperature_input.replace(".","").replace("-","").isdigit():
    temperature = float(temperature_input)
else:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if temperature_type == "F":
    convert_to_celsius(temperature)
elif temperature_type == "C":
    convert_to_fahrenheit(temperature)
else:
    print("Invalid temperature.")


