# Simple U-Value Calculator for a Three-Layer Wall

print("Welcome to the Simple U-Value Calculator!")
print("This calculator determines the U-value of a wall with two layers.")

# Layer 1 input
print("\nLayer 1 (Outer layer):")
thickness1 = float(input("Enter thickness of the layer (in inches): "))
conductivity1 = float(input("Enter thermal conductivity of the material (BTU·in/h·ft²·°F): "))

# Layer 2 input
print("\nLayer 2 (Middle layer):")
thickness2 = float(input("Enter thickness of the layer (in inches): "))
conductivity2 = float(input("Enter thermal conductivity of the material (BTU·in/h·ft²·°F): "))

# Calculate R-values for each layer
r_value1 = thickness1 / conductivity1
r_value2 = thickness2 / conductivity2

# Calculate total R-value
total_r_value = r_value1 + r_value2

# Calculate U-value
u_value = 1 / total_r_value

# Display results
print(f"\nResults:")
print(f"R-value of Layer 1: {r_value1} h·ft²·°F/BTU")
print(f"R-value of Layer 2: {r_value2} h·ft²·°F/BTU")
print(f"Total R-value of the wall: {total_r_value} h·ft²·°F/BTU")
print(f"U-value of the wall: {u_value} BTU/h·ft²·°F")