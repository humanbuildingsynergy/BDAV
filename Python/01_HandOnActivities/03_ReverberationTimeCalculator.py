# Reverberation Time Calculator for Room Acoustics

print("Welcome to the Reverberation Time Calculator!")
print("This calculator estimates the reverberation time of a room using the Sabine formula.")

# Input room dimensions
length = float(input("Enter room length (in feet): "))
width = float(input("Enter room width (in feet): "))
height = float(input("Enter room height (in feet): "))

# Calculate room volume
volume = length * width * height

# Input surface materials and their areas
print("\nEnter the surface areas and absorption coefficients for different materials:")

# Floor
floor_area = length * width
floor_material = input("Enter floor material (e.g., carpet, wood, tile): ")
floor_absorption = float(input(f"Enter absorption coefficient for {floor_material}: "))

# Ceiling
ceiling_area = length * width
ceiling_material = input("Enter ceiling material (e.g., acoustic tile, plaster): ")
ceiling_absorption = float(input(f"Enter absorption coefficient for {ceiling_material}: "))

# Walls (assuming all walls have the same material for simplicity)
wall_area = 2 * (length * height + width * height)
wall_material = input("Enter wall material (e.g., painted, brick, curtain): ")
wall_absorption = float(input(f"Enter absorption coefficient for {wall_material}: "))

# Calculate total absorption
total_absorption = (floor_area * floor_absorption +
                    ceiling_area * ceiling_absorption +
                    wall_area * wall_absorption)

# Calculate reverberation time using Sabine formula
reverberation_time = 0.049 * volume / total_absorption

# Display results
print(f"\nResults:")
print(f"Room Volume: {volume:.2f} cubic feet")
print(f"Total Surface Area: {floor_area + ceiling_area + wall_area:.2f} square feet")
print(f"Total Absorption: {total_absorption:.2f} sabins")
print(f"Estimated Reverberation Time: {reverberation_time:.2f} seconds")