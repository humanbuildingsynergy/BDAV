import matplotlib.pyplot as plt

def get_monthly_data():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months, [float(input(f"{month}: ")) for month in months]

def analyze_consumption(data):
    total = sum(data)
    avg = total / len(data)
    if avg < 500:
        return f"Low consumption. Annual: {total:.0f} kWh, Monthly avg: {avg:.0f} kWh"
    elif avg < 1000:
        return f"Average consumption. Annual: {total:.0f} kWh, Monthly avg: {avg:.0f} kWh"
    else:
        return f"High consumption. Annual: {total:.0f} kWh, Monthly avg: {avg:.0f} kWh"

def plot_energy_consumption(months, data):
    plt.figure(figsize=(10, 5))
    plt.bar(months, data)
    plt.title("Monthly Energy Consumption")
    plt.xlabel("Month")
    plt.ylabel("Energy (kWh)")
    plt.xticks(rotation=45)
    for i, v in enumerate(data):
        plt.text(i, v, f"{v:.0f}", ha='center', va='bottom')
    plt.tight_layout()
    plt.show()

def main():
    print("Building Energy Consumption Analyzer")
    print("Enter monthly energy consumption in kWh:")
    months, energy_data = get_monthly_data()
    
    analysis = analyze_consumption(energy_data)
    print(f"\nAnalysis Results:\n{analysis}")
    
    plot_energy_consumption(months, energy_data)

if __name__ == "__main__":
    main()