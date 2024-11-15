# Energy Efficiency Calculator (IP Units)

# Constants
R_VALUE = 13  # ft²·°F·h/BTU (assuming average insulation)

# Welcome message/;i
print("Welcome to the Energy Efficiency Calculator (IP Units)!")

# Input room dimensions
length = float(input("Enter room length (in feet): "))
width = float(input("Enter room width (in feet): "))
height = float(input("Enter room height (in feet): "))

# Calculate surface areas
floor_ceiling_area = length * width
wall_area = 2 * (length + width) * height
total_area = 2 * floor_ceiling_area + wall_area

# Input temperatures
indoor_temp = float(input("Enter indoor temperature (in °F): "))
outdoor_temp = float(input("Enter outdoor temperature (in °F): "))

# Calculate heat loss (in BTU/h)
total_heat_loss = (total_area / R_VALUE) * (indoor_temp - outdoor_temp)

# Display results
print("\nRoom dimensions:", length, "ft x", width, "ft x", height, "ft")
print("Total surface area:", round(total_area, 2), "ft²")
print("Temperature difference:", round(indoor_temp - outdoor_temp, 1), "°F")
print("Total heat loss:", round(total_heat_loss, 2), "BTU/h")
