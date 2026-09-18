# A simple script that converts Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)

print(f"{temp_c}°C is equal to {temp_f}°F")
