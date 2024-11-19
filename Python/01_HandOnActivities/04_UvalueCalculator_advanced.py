# U-Value Calculator with Functions

def calculate_r_value(thickness, conductivity):
    """Calculate R-value given thickness and conductivity"""
    return thickness / conductivity

def calculate_u_value(total_r_value):
    """Calculate U-value given total R-value"""
    return 1 / total_r_value

def get_layer_input(layer_number):
    """Get input for a single layer"""
    print(f"\nLayer {layer_number}:")
    thickness = float(input("Enter thickness of the layer (in inches): "))
    conductivity = float(input("Enter thermal conductivity of the material (BTU·in/h·ft²·°F): "))
    return thickness, conductivity

def assess_insulation_quality(u_value):
    """Assess insulation quality based on U-value"""
    if u_value < 0.05:
        return "Excellent"
    elif u_value < 0.1:
        return "Good"
    elif u_value < 0.2:
        return "Fair"
    else:
        return "Poor"

def main():
    print("Welcome to the U-Value Calculator!")
    print("This calculator determines the U-value of a wall with three layers.")

    total_r_value = 0

    for i in range(1, 4):
        thickness, conductivity = get_layer_input(i)
        r_value = calculate_r_value(thickness, conductivity)
        total_r_value += r_value
        print(f"R-value of Layer {i}: {r_value:.2f} h·ft²·°F/BTU")

    u_value = calculate_u_value(total_r_value)

    print(f"\nResults:")
    print(f"Total R-value of the wall: {total_r_value:.2f} h·ft²·°F/BTU")
    print(f"U-value of the wall: {u_value:.4f} BTU/h·ft²·°F")

    quality = assess_insulation_quality(u_value)
    print(f"\nInsulation Quality: {quality}")

    if quality in ["Poor", "Fair"]:
        print("\nRecommendation: Consider adding insulation layers to improve energy efficiency.")
    else:
        print("\nRecommendation: Your wall has good insulation properties.")

if __name__ == "__main__":
    main()