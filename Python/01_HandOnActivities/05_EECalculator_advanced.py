# Energy Efficiency Calculator with Functions

def calculate_surface_area(length, width, height):
    """Calculate total surface area of a room"""
    floor_ceiling_area = length * width
    wall_area = 2 * (length + width) * height
    return 2 * floor_ceiling_area + wall_area

def calculate_heat_loss(area, heat_transfer_coefficient, temp_difference):
    """Calculate heat loss through a surface"""
    return heat_transfer_coefficient * area * temp_difference

def get_room_dimensions():
    """Get room dimensions from user input"""
    length = float(input("Enter room length (in feet): "))
    width = float(input("Enter room width (in feet): "))
    height = float(input("Enter room height (in feet): "))
    return length, width, height

def get_temperatures():
    """Get indoor and outdoor temperatures from user input"""
    indoor_temp = float(input("Enter indoor temperature (in °F): "))
    outdoor_temp = float(input("Enter outdoor temperature (in °F): "))
    return indoor_temp, outdoor_temp

def assess_energy_efficiency(heat_loss):
    """Assess energy efficiency based on heat loss"""
    if heat_loss < 5000:
        return "Excellent"
    elif heat_loss < 7500:
        return "Good"
    elif heat_loss < 10000:
        return "Fair"
    else:
        return "Poor"

def main():
    print("Welcome to the Energy Efficiency Calculator!")

    length, width, height = get_room_dimensions()
    indoor_temp, outdoor_temp = get_temperatures()

    total_area = calculate_surface_area(length, width, height)
    temp_difference = indoor_temp - outdoor_temp

    # Assuming a constant heat transfer coefficient for simplicity
    heat_transfer_coefficient = 0.5  # BTU/h·ft²·°F

    total_heat_loss = calculate_heat_loss(total_area, heat_transfer_coefficient, temp_difference)

    print(f"\nResults:")
    print(f"Room dimensions: {length}ft x {width}ft x {height}ft")
    print(f"Total surface area: {total_area:.2f} ft²")
    print(f"Temperature difference: {temp_difference:.1f}°F")
    print(f"Total heat loss: {total_heat_loss:.2f} BTU/h")

    efficiency_rating = assess_energy_efficiency(total_heat_loss)
    print(f"Energy efficiency rating: {efficiency_rating}")

    if efficiency_rating in ["Poor", "Fair"]:
        print("\nRecommendation: Consider improving insulation.")
    else:
        print("\nRecommendation: Your room has good energy efficiency.")

print(__name__)
if __name__ == "__main__":
    main()