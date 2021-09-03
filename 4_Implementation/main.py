"""
Main function for MiniCarWale
"""
import cars
print("\n" + "--Welcome to Mini CarWale--" + "\n")
print("Choose Your Car and get more details")
print("View Price Breakup and EMI Calculations")
print("Choose Brand of your Car")
print("1. TATA" + "\n" + "2. Maruti" + "\n" + "3. Skoda" + "\n" + "4. Honda" + "\n" + "5. Hyundai")
CHOICE = int(input("Enter your choice : "))
cars.totalcars(CHOICE)
